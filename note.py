import speech_recognition as sr
from datetime import datetime

def listen_and_transcribe():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak now (say 'stop listening' to end)...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    
    try:
        text = recognizer.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return "Error: Speech Recognition service unavailable"

def format_note(transcribed_text):
    note = ""
    
    if transcribed_text.startswith("heading"):
        heading = transcribed_text.replace("heading", "").strip().title()
        note += f"\n# {heading}\n"
    
    elif transcribed_text.startswith("subheading"):
        subheading = transcribed_text.replace("subheading", "").strip().title()
        note += f"\n## {subheading}\n"
    
    elif transcribed_text.startswith("point"):
        point = transcribed_text.replace("point", "").strip().capitalize()
        note += f"- {point}\n"
        
    elif transcribed_text.startswith("paragraph"):
        paragraph = transcribed_text.replace("paragraph", "").strip()
        note += f"\n{paragraph.capitalize()}\n"
    else:
        # Treat everything else like a paragraph
        note += f"\n{transcribed_text.capitalize()}\n"
    
    return note


if __name__ == "__main__":
    final_note = f"### Notes taken on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"

    while True:
        text = listen_and_transcribe()
        
        if "stop listening" in text:
            print("🛑 Stopped listening.")
            break

        if text:
            formatted = format_note(text)
            final_note += formatted
            print(formatted)

    # Save notes into file
    with open("voice_notes.md", "w", encoding="utf-8") as f:
        f.write(final_note)

    print("\n✅ Notes saved as 'voice_notes.md'")
