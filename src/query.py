import whisper
import warnings
warnings.filterwarnings("ignore")
from state import State
from record import record_audio_to_mp3

model = whisper.load_model("tiny")  

def transcribe(audio):
    text = model.transcribe(audio)['text']
    print(text)
    return text


def get_query(state:State):
    choice = input("Enter the choice 1 for audio any button for text")
    if choice=='1':
        record_audio_to_mp3(duration = 50)
        question = transcribe("my_recording.mp3")
    question = input("Enter your query")
    return {'query':question}
