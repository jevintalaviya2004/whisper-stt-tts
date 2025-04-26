# whisper_stt.py
import openai
import speech_recognition as sr

openai.api_key = ""  # Replace with your API key

# Function to record audio until silence
def record_until_silence():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("🎙️ Listening... Speak now. (Pause to stop recording)")

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)  # noise handling
        audio = recognizer.listen(source, timeout=None)  # wait until silence

    print("✅ Recording finished.")

    # Return the audio data directly
    return audio.get_wav_data()

# Function to transcribe audio using Whisper
def transcribe_with_whisper(audio_data):
    print("🧠 Transcribing with Whisper...")
    # Pass the audio data directly to Whisper
    transcript = openai.Audio.transcribe("whisper-1", audio_data)
    return transcript["text"]
