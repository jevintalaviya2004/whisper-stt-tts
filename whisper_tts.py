# whisper_tts.py
import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Function for text-to-speech
def text_to_speech(text):
    try:
        # Set properties (optional)
        engine.setProperty('rate', 150)  # Speed of speech
        engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

        # Save the speech to an audio file
        response_audio = 'response.mp3'
        engine.save_to_file(text, response_audio)
        engine.runAndWait()

        # Return the file path
        return response_audio
    except Exception as e:
        return str(e)
