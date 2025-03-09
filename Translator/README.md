# AI-Powered Translator GUI Application

This Python-based GUI application leverages the OpenAI API to translate text accurately while preserving the original meaning. Built with PyQt5, it offers an intuitive and feature-rich user interface designed to streamline text translation tasks.

## Key Features

### Core Functionalities:
- **Text Translation:** Translate text between multiple languages using OpenAI's advanced language models.
- **Batch Translation:** Efficiently translate multiple text files simultaneously.
- **Auto Language Detection:** Automatically identifies the language of input text.
- **Speech-to-Text:** Input text via voice using microphone support.
- **Text-to-Speech:** Converts translated text into audio files (MP3).
- **Translation History:** Keeps track of all previous translations.
- **Cost Estimation:** Calculates and displays the approximate cost of each translation request based on token usage.
- **Feedback Mechanism:** Enables users to submit feedback to improve future translations.
- **Progress Visualization:** Provides real-time translation progress via a progress bar, especially useful for batch translations.

## Features

- **File Operations:** Open and save translated texts.
- **Clipboard Support:** Easy copying of translated content.
- **Automatic Language Detection:** Integrated language detection for convenience.

## Technologies Used

- **Python 3.x**
- **PyQt5** for GUI development
- **OpenAI GPT API** for translations
- **SpeechRecognition** for speech-to-text
- **gTTS** for text-to-speech
- **langdetect** for automatic language detection

## Setup and Installation

### Prerequisites
- Python 3.x installed
- Install dependencies:

```bash
pip install PyQt5 openai SpeechRecognition gTTS langdetect
```

## Running the Application

```bash
python translator_app.py
```

## Usage Instructions

1. Open or type the text you wish to translate.
2. Select the target language from the dropdown.
3. Click **Translate**.
4. Use advanced features such as batch translation, text-to-speech, and more via dedicated buttons.

## Notes
- Replace the provided OpenAI API key with your own secure key.
- API costs shown are estimated based on token counts and current pricing (subject to change by OpenAI).

## Feedback and Contributions
Contributions and feedback are welcomed to enhance the application's functionality and performance.

