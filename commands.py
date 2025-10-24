import webbrowser
import wikipedia
from text_to_speech import speak
from utils.helper_functions import get_current_time, get_current_date, clean_query

def execute_command(query):
    """
    Executes a command based on the user query.
    Returns 'exit' if the user wants to quit.
    """
    query = query.lower()  # ensure consistent matching

    if 'time' in query:
        current_time = get_current_time()
        speak(f"The current time is {current_time}")

    elif 'date' in query:
        today = get_current_date()
        speak(f"Today's date is {today}")

    elif 'open google' in query:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif 'open youtube' in query:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif 'wikipedia' in query:
        speak("Searching Wikipedia...")
        topic = clean_query(query)  # remove 'wikipedia' and extra spaces
        try:
            result = wikipedia.summary(topic, sentences=2)
            speak(result)
        except Exception:
            speak("Sorry, I could not find information on Wikipedia.")

    elif 'exit' in query or 'quit' in query:
        speak("Goodbye!")
        return "exit"

    else:
        speak("Sorry, I did not understand the command.")
