import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTextEdit, QFileDialog, QLabel, QComboBox, QMessageBox, QProgressBar, QDialog, QInputDialog
)
from PyQt5.QtCore import Qt
from openai import OpenAI

# Initialize the OpenAI client with your test API key.
client = OpenAI(
    api_key="TOKEN"
)


class TranslatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Translator")
        self.resize(1000, 700)
        self.translation_history = []
        self.feedback_list = []
        self.initUI()

    def initUI(self):
        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout()
        main_widget.setLayout(main_layout)

        # Input text field
        self.input_text_edit = QTextEdit()
        self.input_text_edit.setPlaceholderText("Enter or load text to translate...")
        main_layout.addWidget(QLabel("Original Text:"))
        main_layout.addWidget(self.input_text_edit)

        # Target language selection
        self.language_combo = QComboBox()
        self.language_combo.addItems(["Spanish", "French", "German", "Chinese", "Japanese"])
        self.language_combo.currentIndexChanged.connect(self.change_target_language)
        language_layout = QHBoxLayout()
        language_layout.addWidget(QLabel("Target Language:"))
        language_layout.addWidget(self.language_combo)
        main_layout.addLayout(language_layout)

        # Translate button
        self.translate_button = QPushButton("Translate")
        self.translate_button.clicked.connect(self.translate_and_display)
        main_layout.addWidget(self.translate_button)

        # Output text field
        self.output_text_edit = QTextEdit()
        self.output_text_edit.setPlaceholderText("Translated text will appear here...")
        main_layout.addWidget(QLabel("Translated Text:"))
        main_layout.addWidget(self.output_text_edit)

        # Buttons for file operations and clipboard
        button_layout = QHBoxLayout()
        self.open_button = QPushButton("Open File")
        self.open_button.clicked.connect(self.open_file)
        button_layout.addWidget(self.open_button)

        self.save_button = QPushButton("Save File")
        self.save_button.clicked.connect(self.save_file)
        button_layout.addWidget(self.save_button)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_text)
        button_layout.addWidget(self.clear_button)

        self.copy_button = QPushButton("Copy to Clipboard")
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        button_layout.addWidget(self.copy_button)

        main_layout.addLayout(button_layout)

        # Advanced functionalities layout
        adv_layout = QHBoxLayout()

        self.batch_button = QPushButton("Batch Translate")
        self.batch_button.clicked.connect(self.batch_translate)
        adv_layout.addWidget(self.batch_button)

        self.tts_button = QPushButton("Text to Speech")
        self.tts_button.clicked.connect(self.text_to_speech)
        adv_layout.addWidget(self.tts_button)

        self.stt_button = QPushButton("Speech to Text")
        self.stt_button.clicked.connect(self.speech_to_text)
        adv_layout.addWidget(self.stt_button)

        self.auto_detect_button = QPushButton("Auto Language Detection")
        self.auto_detect_button.clicked.connect(self.auto_language_detection)
        adv_layout.addWidget(self.auto_detect_button)

        self.history_button = QPushButton("Translation History")
        self.history_button.clicked.connect(self.show_translation_history)
        adv_layout.addWidget(self.history_button)

        self.cost_button = QPushButton("Show Translation Cost")
        self.cost_button.clicked.connect(self.show_translation_cost)
        adv_layout.addWidget(self.cost_button)

        self.feedback_button = QPushButton("Feedback")
        self.feedback_button.clicked.connect(self.translation_quality_feedback)
        adv_layout.addWidget(self.feedback_button)

        main_layout.addLayout(adv_layout)

        # Progress bar for batch translation
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        main_layout.addWidget(self.progress_bar)

    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open Text File", "", "Text Files (*.txt);;All Files (*)", options=options
        )
        if file_name:
            try:
                with open(file_name, "r", encoding="utf-8") as f:
                    content = f.read()
                    self.input_text_edit.setPlainText(content)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to open file:\n{str(e)}")

    def save_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Save Translated Text", "", "Text Files (*.txt);;All Files (*)", options=options
        )
        if file_name:
            try:
                with open(file_name, "w", encoding="utf-8") as f:
                    f.write(self.output_text_edit.toPlainText())
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to save file:\n{str(e)}")

    def translate_and_display(self):
        original_text = self.input_text_edit.toPlainText()
        if not original_text.strip():
            QMessageBox.warning(self, "Warning", "Please enter some text to translate.")
            return

        target_language = self.language_combo.currentText()
        prompt = f"Translate the following text into {target_language} while preserving its original meaning:\n\n{original_text}"

        try:
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                store=True,
                messages=[
                    {"role": "system", "content": "You are a helpful translation assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            translated_text = completion.choices[0].message['content'].strip()
            self.output_text_edit.setPlainText(translated_text)
            # Save to translation history
            self.translation_history.append({
                "file": "Manual Input",
                "original": original_text,
                "translated": translated_text,
                "language": target_language
            })
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Translation failed:\n{str(e)}")

    def clear_text(self):
        self.input_text_edit.clear()
        self.output_text_edit.clear()

    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.output_text_edit.toPlainText())
        QMessageBox.information(self, "Copied", "Translated text copied to clipboard.")

    def change_target_language(self):
        selected_language = self.language_combo.currentText()
        print(f"Target language changed to: {selected_language}")

    def batch_translate(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select Text Files", "", "Text Files (*.txt)")
        if not files:
            return
        # Clear existing history and progress bar
        self.translation_history.clear()
        self.progress_bar.setMaximum(len(files))
        self.progress_bar.setValue(0)
        results = ""
        target_language = self.language_combo.currentText()
        for i, file_name in enumerate(files, start=1):
            try:
                with open(file_name, "r", encoding="utf-8") as f:
                    content = f.read()
                prompt = f"Translate the following text into {target_language} while preserving its original meaning:\n\n{content}"
                completion = client.chat.completions.create(
                    model="gpt-4o-mini",
                    store=True,
                    messages=[
                        {"role": "system", "content": "You are a helpful translation assistant."},
                        {"role": "user", "content": prompt}
                    ]
                )
                translated_text = completion.choices[0].message['content'].strip()
                results += f"File: {file_name}\nOriginal:\n{content}\nTranslated:\n{translated_text}\n{'-' * 40}\n"
                # Save to translation history
                self.translation_history.append({
                    "file": file_name,
                    "original": content,
                    "translated": translated_text,
                    "language": target_language
                })
                self.progress_bar.setValue(i)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to translate {file_name}:\n{str(e)}")
        self.output_text_edit.setPlainText(results)

    def text_to_speech(self):
        from gtts import gTTS
        text = self.output_text_edit.toPlainText()
        if not text.strip():
            QMessageBox.warning(self, "Warning", "No translated text available for conversion.")
            return
        try:
            tts = gTTS(text)
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getSaveFileName(
                self, "Save Audio File", "", "MP3 Files (*.mp3);;All Files (*)", options=options
            )
            if file_name:
                tts.save(file_name)
                QMessageBox.information(self, "Success", f"Audio saved to {file_name}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Text-to-speech conversion failed:\n{str(e)}")

    def speech_to_text(self):
        import speech_recognition as sr
        r = sr.Recognizer()
        with sr.Microphone() as source:
            QMessageBox.information(self, "Info", "Please speak now...")
            audio = r.listen(source)
        try:
            recognized_text = r.recognize_google(audio)
            self.input_text_edit.setPlainText(recognized_text)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Speech recognition failed:\n{str(e)}")

    def auto_language_detection(self):
        from langdetect import detect
        text = self.input_text_edit.toPlainText()
        if not text.strip():
            QMessageBox.warning(self, "Warning", "No text available for language detection.")
            return
        try:
            detected_language = detect(text)
            QMessageBox.information(self, "Language Detection", f"Detected language: {detected_language}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Language detection failed:\n{str(e)}")

    def show_translation_history(self):
        if not self.translation_history:
            QMessageBox.information(self, "History", "No translations in history yet.")
            return
        history_str = ""
        for entry in self.translation_history:
            history_str += (f"File: {entry['file']}\n"
                            f"Language: {entry['language']}\n"
                            f"Original:\n{entry['original']}\n"
                            f"Translated:\n{entry['translated']}\n"
                            + "-" * 40 + "\n")
        dialog = QDialog(self)
        dialog.setWindowTitle("Translation History")
        layout = QVBoxLayout()
        text_edit = QTextEdit()
        text_edit.setReadOnly(True)
        text_edit.setPlainText(history_str)
        layout.addWidget(text_edit)
        dialog.setLayout(layout)
        dialog.exec_()

    def show_translation_cost(self):
        text = self.input_text_edit.toPlainText()
        if not text.strip():
            QMessageBox.warning(self, "Warning", "No text available to calculate cost.")
            return
        # Estimate cost based on word count (as a rough proxy for tokens)
        estimated_tokens = len(text.split())
        cost_per_1000_tokens = 0.02  # Example cost rate in USD
        estimated_cost = (estimated_tokens / 1000) * cost_per_1000_tokens
        QMessageBox.information(
            self, "Translation Cost",
            f"Estimated translation cost: ${estimated_cost:.4f} USD (based on {estimated_tokens} tokens)"
        )

    def translation_quality_feedback(self):
        feedback, ok = QInputDialog.getMultiLineText(
            self, "Translation Feedback", "Enter your feedback about the translation:"
        )
        if ok and feedback.strip():
            self.feedback_list.append(feedback)
            QMessageBox.information(self, "Feedback Received", "Thank you for your feedback!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    translator_app = TranslatorApp()
    translator_app.show()
    sys.exit(app.exec_())