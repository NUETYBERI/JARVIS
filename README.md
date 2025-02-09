Project Overview: AI Voice Assistant (Jarvis)
This project is an AI-powered voice assistant that can recognize speech, process commands, and interact via voice and text. It includes face authentication, hotword detection, and chatbot capabilities.

🔹Technologies Used
 
1. Backend (Python)
- Flask & Eel → Connects Python with JavaScript for real-time interactions.
- Speech Recognition (speech_recognition library) → Converts voice input to text.
- Text-to-Speech (pyttsx3) → Converts responses into speech output.
- Face Authentication (opencv & dlib) → Recognizes users before starting the assistant.
- Porcupine (pvporcupine) → Detects wake words like "Jarvis".
- SQLite3 → Stores commands and contacts for quick retrieval.
- Google Gemini API → Provides chatbot responses.
- Pywhatkit → Plays YouTube videos based on voice commands.

2. Frontend (JavaScript, HTML, CSS)
- Bootstrap → For responsive UI.
- SiriWave.js → Generates animated Siri-like voice waves.
- Textillate.js → Adds text animations.
- Lottie.js → Displays animations during authentication.
- jQuery & AJAX → Handles real-time UI updates and interactions.

🔹 Machine Learning Techniques Used

- Face Recognition (Deep Learning)
- Uses OpenCV & Dlib to detect and verify faces for authentication.
- Natural Language Processing (NLP)
- Uses Google Gemini API for understanding and responding to queries.
- Hotword Detection (Keyword Spotting)
- Uses Porcupine AI to listen for "Jarvis" or "Alexa".

🔹 Project Flow

- Startup & Authentication
- Plays assistant sound.
- Authenticates user via face recognition.
- Greets the user after authentication.
- Listening for Commands
- Detects wake word ("Jarvis" or "Alexa").
- Converts voice to text.
- Processes the command.
- Executing Actions
- Opens apps, websites, or performs chatbot tasks.
- Sends responses via voice and text.
- Frontend Interaction
- Displays real-time responses in chat format.
- Uses animations and wave effects for a modern UI.

🔹 Conclusion

This project integrates Machine Learning, NLP, and Web Technologies to create an interactive AI assistant with real-time responses and a futuristic UI. 
