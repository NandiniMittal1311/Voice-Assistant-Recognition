from utils.audio_processing import listen_from_microphone

def listen():
    """
    Wrapper function to call audio processing and return the recognized text.
    """
    query = listen_from_microphone()
    return query

# Optional: test this file independently
if __name__ == "__main__":
    text = listen()
    print(f"Recognized text: {text}")
