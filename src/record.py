import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment
import os

def record_audio_to_mp3(filename="output.mp3", duration=5, sample_rate=44100, channels=2):
    """
    Records audio from the microphone and saves it as an MP3 file.

    Args:
        filename (str): Output MP3 file name.
        duration (int): Duration of the recording in seconds.
        sample_rate (int): Sampling rate in Hz.
        channels (int): Number of audio channels (1=Mono, 2=Stereo).
    """
    wav_filename = filename.replace(".mp3", ".wav")

    print(f"🎤 Recording for {duration} seconds...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
    sd.wait()
    print("✅ Recording complete.")

    
    write(wav_filename, sample_rate, audio)

    
    sound = AudioSegment.from_wav(wav_filename)
    sound.export(filename, format="mp3")
    print(f"💾 Saved MP3 as: {filename}")

    
    os.remove(wav_filename)


