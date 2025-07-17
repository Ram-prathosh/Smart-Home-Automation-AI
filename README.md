
# Smart-Home-Automation-AI 🔊🏡

An AI-powered voice-controlled smart home automation system built using Python. This project allows users to control simulated devices like lights, fan, and AC through voice commands and includes basic energy-saving suggestions based on the time of day.

---

## 💡 Features

- 🎤 Voice command recognition using `speech_recognition`
- 🗣️ Text-to-speech feedback using `pyttsx3`
- ⏰ Time-based automation suggestions
- 📋 Device status report
- 🧠 Intelligent command interpretation

---

## 🛠️ Technologies Used

- [Python 3.x](https://www.python.org/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [PyAudio](https://pypi.org/project/PyAudio/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Smart-Home-Automation-AI.git
cd Smart-Home-Automation-AI
```

### 2. Install dependencies

Ensure Python is installed. Then run:

```bash
pip install -r requirements.txt
```

**`requirements.txt` should include:**
```
SpeechRecognition
pyttsx3
pyaudio
```

> ⚠️ Note: Installing `PyAudio` might require system-specific setup. Use `pipwin install pyaudio` on Windows if needed.

### 3. Run the program

```bash
python smart_home.py
```

---

## 🎙️ Available Voice Commands

- `Turn on lights`
- `Turn off lights`
- `Turn on fan`
- `Turn off fan`
- `Turn on AC`
- `Turn off AC`
- `Status` – Get the current state of all devices

---

## 📸 Screenshot

> *(Optional)* You can add a screenshot of your CLI in use here:
```
assets/screenshot.png
```

---

## ✅ Future Improvements

- Real IoT integration with MQTT or Raspberry Pi
- GUI interface using Tkinter or PyQt
- NLP support for flexible command parsing
- Add user-specific profiles and scheduling

---


