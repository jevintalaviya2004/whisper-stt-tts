from flask import Flask, request, jsonify
import pyttsx3
import openai
from whisper_stt import record_until_silence, transcribe_with_whisper
from whisper_tts import text_to_speech
from src.faiss_retrieval import load_index
from src.response_generator import generate_response, retrieve_context

# Initialize Flask app
app = Flask(__name__)

# Initialize Whisper and TTS engine
openai.api_key = "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"
tts_engine = pyttsx3.init()

# Function to speak TTS response
def speak_response(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Home route for the chatbot
@app.route('/')
def home():
    return "Welcome to the RAG Chatbot! Use /ask endpoint to chat."

# Ask route to handle chat requests
@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()

        if not data or 'query' not in data:
            return jsonify({"error": "Invalid input. Please send a JSON with a 'query' field."}), 400

        query = data['query']

        # If the query is audio, capture the audio and transcribe it
        if query == 'audio':
            audio_data = record_until_silence()  # Record audio using speech recognition
            query = transcribe_with_whisper(audio_data)  # Convert speech to text using Whisper

        # Step 1: Retrieve context based on the query
        context = retrieve_context(query)

        # Step 2: Generate the response based on the context
        answer = generate_response(query, context)

        # Step 3: Speak the generated response using TTS
        speak_response(answer)

        # Step 4: Return the text answer as a JSON response
        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
