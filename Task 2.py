import speech_recognition as sr

def record_and_transcribe():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("🎙 Speak now... (Recording for 5 seconds)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, phrase_time_limit=5)

    try:
        print("🧠 Transcribing...")
        text = recognizer.recognize_google(audio)
        print("✅ Transcription:")
        print(text)
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
    except sr.RequestError as e:
        print(f"❌ Could not request results; {e}")

# Run it
record_and_transcribe()