from datetime import datetime
from google.cloud import speech
from google.protobuf import wrappers_pb2
from google.cloud import texttospeech_v1
from flask import Flask, render_template, request, redirect, url_for, send_file, send_from_directory
from werkzeug.utils import secure_filename
from google.cloud import language_v2
import os


client=speech.SpeechClient()

def sentiment(text):
    sentiment = sample_analyze_sentiment(text)

    score = sentiment.document_sentiment.score * sentiment.document_sentiment.magnitude


    if score > 0.75:
        return "POSITIVE"
    elif score < -0.75:
        return "NEGATIVE"
    else:
        return "NEUTRAL"

def sample_analyze_sentiment(text_content):
    """
    Analyzes Sentiment in a string.

    Args:
      text_content: The text content to analyze.
    """

    client = language_v2.LanguageServiceClient()

    # text_content = 'I am so happy and joyful.'

    # Available types: PLAIN_TEXT, HTML
    document_type_in_plain_text = language_v2.Document.Type.PLAIN_TEXT

    # Optional. If not specified, the language is automatically detected.
    # For list of supported languages:
    # https://cloud.google.com/natural-language/docs/languages
    language_code = "en"
    document = {
        "content": text_content,
        "type_": document_type_in_plain_text,
        "language_code": language_code,
    }

    # Available values: NONE, UTF8, UTF16, UTF32
    # See https://cloud.google.com/natural-language/docs/reference/rest/v2/EncodingType.
    encoding_type = language_v2.EncodingType.UTF8

    response = client.analyze_sentiment(
        request={"document": document, "encoding_type": encoding_type}
    )
    # Get overall sentiment of the input document
    print(f"Document sentiment score: {response.document_sentiment.score}")
    print(f"Document sentiment magnitude: {response.document_sentiment.magnitude}")
    # Get sentiment for all sentences in the document
    for sentence in response.sentences:
        print(f"Sentence text: {sentence.text.content}")
        print(f"Sentence sentiment score: {sentence.sentiment.score}")
        print(f"Sentence sentiment magnitude: {sentence.sentiment.magnitude}")

    # Get the language of the text, which will be the same as
    # the language specified in the request or, if not specified,
    # the automatically-detected language.
    print(f"Language of the text: {response.language_code}")

    return response

def sample_recognize(content):
  audio=speech.RecognitionAudio(content=content)

  config=speech.RecognitionConfig(
  # encoding=speech.RecognitionConfig.AudioEncoding.MP3,
  # sample_rate_hertz=24000,
  language_code="en-US",
  model="latest_long",
  audio_channel_count=1,
  enable_word_confidence=True,
  enable_word_time_offsets=True,
  )

  operation=client.long_running_recognize(config=config, audio=audio)

  response=operation.result(timeout=90)

  txt = ''
  for result in response.results:
    txt = txt + result.alternatives[0].transcript + '\n'

  return txt

client2 = texttospeech_v1.TextToSpeechClient()

def sample_synthesize_speech(text=None, ssml=None):
    input = texttospeech_v1.SynthesisInput()
    if ssml:
      input.ssml = ssml
    else:
      input.text = text

    voice = texttospeech_v1.VoiceSelectionParams()
    voice.language_code = "en-UK"
    # voice.ssml_gender = "MALE"

    audio_config = texttospeech_v1.AudioConfig()
    audio_config.audio_encoding = "LINEAR16"

    request = texttospeech_v1.SynthesizeSpeechRequest(
        input=input,
        voice=voice,
        audio_config=audio_config,
    )

    response = client2.synthesize_speech(request=request)

    return response.audio_content


app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'wav'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

RESULTS = 'result'
ALLOWED_EXTENSIONS = {'wav'}
app.config['RESULTS'] = RESULTS

os.makedirs(RESULTS, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_files():
    files = []
    for filename in os.listdir(UPLOAD_FOLDER):
        if allowed_file(filename):
            files.append(filename)
            print(filename)
    files.sort(reverse=True)
    return files

def get_rfiles():
    files = []
    for filename in os.listdir(RESULTS):
        if allowed_file(filename):
            files.append(filename)
            print(filename)
    files.sort(reverse=True)
    return files

@app.route('/')
def index():
    files = get_files()
    rfiles = get_rfiles()
    return render_template('index.html', files=files, rfiles=rfiles)

@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'audio_data' not in request.files:
        flash('No audio data')
        return redirect(request.url)
    file = request.files['audio_data']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file:
        # filename = secure_filename(file.filename)
        filename = datetime.now().strftime("%Y%m%d-%I%M%S%p") + '.wav'
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        f = open(file_path,'rb')
        data = f.read()
        f.close()

        text = sample_recognize(data)

        sentiment_path= file_path+".sen"+".txt"
        f=open(sentiment_path,"w")
        f.write(sentiment(text))
        f.close()


        f = open(file_path+'.txt','w')
        f.write(text)
        f.close()

    return redirect('/') #success

@app.route('/upload/<filename>')
def get_file(filename):
    return send_file(filename)

@app.route('/results/<filename>')
def get_rfile(filename):
    return send_file(filename)

    
@app.route('/upload_text', methods=['POST'])
def upload_text():
    text = request.form['text']
    print(text)
    filename = datetime.now().strftime("%Y%m%d-%I%M%S%p") + '.wav'
    file_path = os.path.join(app.config['RESULTS'], filename)

    wav = sample_synthesize_speech(text)

    # save audio
    f = open(file_path,'wb')
    f.write(wav)
    f.close()

    #save text
    f = open(file_path+'.txt','w')
    f.write(text)
    f.close()

    sentiment_path= file_path+".sen"+".txt"
    f=open(sentiment_path,"w")
    f.write(sentiment(text))
    f.close()

    return redirect('/') #success

@app.route('/script.js',methods=['GET'])
def scripts_js():
    return send_file('./script.js')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/result/<filename>')
def uploaded_rfile(filename):
    return send_from_directory(app.config['RESULTS'], filename)

if __name__ == '__main__':
    app.run(debug=True)