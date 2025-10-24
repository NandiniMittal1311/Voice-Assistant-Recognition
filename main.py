from speech_to_text import listen
from text_to_speech import speak
from commands import execute_command

if __name__ == "__main__":
    speak("Hello! I am your voice assistant. How can I help you?")
    while True:
        query = listen()
        if query:
            result = execute_command(query)
            if result == "exit":
                break
