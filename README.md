# 🎤 Voice Note Taker

## 📌 Project Overview
**Voice Note Taker** is a Python-based tool that listens to your voice, converts it into text, and automatically formats the text into structured notes.  
It supports **Headings, Subheadings, Paragraphs, and Bullet Points** using simple voice commands like:

- `"Heading Artificial Intelligence"` → Creates a main heading  
- `"Subheading Machine Learning"` → Creates a subheading  
- `"Paragraph Artificial intelligence is a field of computer science …"` → Adds a paragraph  
- `"Point It learns from data"` → Adds a bullet point  
- `"Stop listening"` → Stops recording and saves notes  

The notes are saved in a **Markdown file (`voice_notes.md`)** which can be opened in any editor, browser, or converted to PDF/Word.

---

## ⚙️ Technologies Used
- **Python 3** – Core programming language  
- **SpeechRecognition** – To capture and transcribe voice into text  
- **Google Web Speech API** – Backend used by SpeechRecognition for transcription  
- **Datetime** – To timestamp notes  
- **Markdown Format** – For structured and readable notes  

---

## 🚀 How to Run
1. Install dependencies:
   ```bash
   pip install SpeechRecognition pyaudio
   ```
   > Note: On Windows, you may need to install PyAudio separately with a wheel file.  

2. Run the program:
   ```bash
   python voice_note_taker.py
   ```

3. Start speaking and use keywords (`heading`, `subheading`, `point`, `paragraph`).  

4. Say **“stop listening”** to finish and save your notes.  

5. Open the generated `voice_notes.md` file.  

---

## 🛠 Practical Uses
This project can be applied in many **real-life situations**:

- **Students** → Take lecture notes hands-free  
- **Researchers** → Dictate research ideas and automatically structure them  
- **Writers/Authors** → Draft chapters or outlines using just voice  
- **Meeting Notes** → Quickly capture meeting points in structured format  
- **Accessibility** → Helps people with physical disabilities take notes without typing  

---

## 📖 Example Output
If you speak the following:

- "Heading Artificial Intelligence"  
- "Subheading Machine Learning"  
- "Paragraph Artificial intelligence is a field of computer science that enables machines to learn and perform tasks."  
- "Point It learns from data"  
- "Point It improves over time"  

The file **`voice_notes.md`** will look like:

```markdown
### Notes taken on 2025-09-13

# Artificial Intelligence

## Machine Learning

Artificial intelligence is a field of computer science that enables machines to learn and perform tasks.

- It learns from data
- It improves over time
```
