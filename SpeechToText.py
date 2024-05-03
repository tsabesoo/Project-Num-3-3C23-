
import speech_recognition as sr


def speech_to_text():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Capture audio from the microphone
    with sr.Microphone() as source:
        print("Please start speaking...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio_data = recognizer.listen(source)

    try:
        # Recognize speech using Google Speech Recognition
        text = recognizer.recognize_google(audio_data)
        return text
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand what you said."
    except sr.RequestError as e:
        return f"Sorry, an error occurred: {e}"

# Test the function
result = speech_to_text()
print("You said:", result)

