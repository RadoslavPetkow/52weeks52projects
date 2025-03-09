#!/usr/bin/env python
import sys
import re
import urllib.request
from youtube_transcript_api import YouTubeTranscriptApi

from PyQt5.QtCore import QThread, pyqtSignal, Qt
from PyQt5.QtGui import QPixmap, QPalette, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTextEdit, QMessageBox, QFileDialog,
    QComboBox, QCheckBox, QGroupBox, QFrame, QStyleFactory
)


def extract_video_id(url):
    """
    Extracts the YouTube video ID from a given URL.
    Supports both standard and shortened URLs.
    """
    pattern = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None


def get_transcript(video_id, language='en'):
    """
    Retrieves the transcript for the given YouTube video ID.
    Returns the concatenated transcript text.
    """
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=[language])
    transcript_text = " ".join([entry['text'] for entry in transcript_list])
    return transcript_text


# Worker thread to fetch transcript without freezing the UI
class TranscriptFetcher(QThread):
    transcript_fetched = pyqtSignal(str)
    error_occurred = pyqtSignal(str)

    def __init__(self, video_id, language='en'):
        super().__init__()
        self.video_id = video_id
        self.language = language

    def run(self):
        try:
            transcript = get_transcript(self.video_id, self.language)
            self.transcript_fetched.emit(transcript)
        except Exception as e:
            self.error_occurred.emit(str(e))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Transcript Fetcher")
        self.setGeometry(100, 100, 900, 600)
        self.transcript = ""
        self.setup_ui()

    def setup_ui(self):
        # Set a main widget and apply a vertical layout
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.main_layout = QVBoxLayout(self.main_widget)
        self.main_widget.setLayout(self.main_layout)

        # Title Section: A banner frame for the header
        self.banner_frame = QFrame()
        self.banner_frame.setObjectName("bannerFrame")
        self.banner_layout = QHBoxLayout()
        self.banner_frame.setLayout(self.banner_layout)

        self.header_label = QLabel("YouTube Transcript Fetcher")
        self.header_label.setObjectName("headerLabel")
        self.header_label.setAlignment(Qt.AlignCenter)

        self.banner_layout.addWidget(self.header_label)
        self.main_layout.addWidget(self.banner_frame)

        # Description below the header
        self.description_label = QLabel("Easily fetch and save YouTube transcripts with a single click.")
        self.description_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.description_label)

        # Group box for URL input
        self.url_group = QGroupBox("Video URL")
        self.url_group_layout = QHBoxLayout()
        self.url_group.setLayout(self.url_group_layout)

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter YouTube URL here...")
        self.fetch_button = QPushButton("Fetch Transcript")
        self.fetch_button.clicked.connect(self.fetch_transcript)

        self.url_group_layout.addWidget(self.url_input)
        self.url_group_layout.addWidget(self.fetch_button)
        self.main_layout.addWidget(self.url_group)

        # Group box for Video Thumbnail
        self.thumbnail_group = QGroupBox("Video Preview")
        self.thumbnail_layout = QVBoxLayout()
        self.thumbnail_group.setLayout(self.thumbnail_layout)

        self.thumbnail_label = QLabel()
        self.thumbnail_label.setAlignment(Qt.AlignCenter)
        self.thumbnail_layout.addWidget(self.thumbnail_label)
        self.main_layout.addWidget(self.thumbnail_group)

        # Group box for Transcript display
        self.transcript_group = QGroupBox("Transcript")
        self.transcript_group_layout = QVBoxLayout()
        self.transcript_group.setLayout(self.transcript_group_layout)

        self.transcript_display = QTextEdit()
        self.transcript_display.setReadOnly(True)
        self.transcript_group_layout.addWidget(self.transcript_display)
        self.main_layout.addWidget(self.transcript_group)

        # Group box for Actions (Save + Status)
        self.actions_group = QGroupBox("Actions")
        self.actions_layout = QHBoxLayout()
        self.actions_group.setLayout(self.actions_layout)

        self.save_button = QPushButton("Save Transcript")
        self.save_button.clicked.connect(self.save_transcript)
        self.status_label = QLabel("Ready")

        self.actions_layout.addWidget(self.save_button)
        self.actions_layout.addWidget(self.status_label)
        self.main_layout.addWidget(self.actions_group)

        # Group box for Settings (Language + Theme)
        self.settings_group = QGroupBox("Settings")
        self.settings_layout = QHBoxLayout()
        self.settings_group.setLayout(self.settings_layout)

        self.language_label = QLabel("Language:")
        self.language_combo = QComboBox()
        self.language_combo.addItems(["en", "es", "fr", "de", "it"])  # Example languages

        self.theme_toggle = QCheckBox("Dark Mode")
        self.theme_toggle.stateChanged.connect(self.toggle_theme)

        self.settings_layout.addWidget(self.language_label)
        self.settings_layout.addWidget(self.language_combo)
        self.settings_layout.addStretch(1)
        self.settings_layout.addWidget(self.theme_toggle)
        self.main_layout.addWidget(self.settings_group)

        # Apply a custom style sheet for a more modern look
        self.apply_style_sheet()

    def apply_style_sheet(self):
        """
        Applies a style sheet to give the UI a more modern, consistent look.
        """
        self.setStyleSheet("""
            /* Overall Window Style */
            QMainWindow {
                background-color: #f7f7f7;
            }

            /* Banner Frame */
            #bannerFrame {
                background-color: #1976D2; /* A modern blue color */
                padding: 12px;
            }
            /* Header Label in Banner */
            #headerLabel {
                color: white;
                font-size: 22px;
                font-weight: 600;
                letter-spacing: 0.5px;
            }

            /* Group Boxes */
            QGroupBox {
                font: 14px 'Arial';
                font-weight: bold;
                margin-top: 10px;
                border: 1px solid #ccc;
                border-radius: 8px;
                padding: 10px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 2px 5px;
            }

            /* Labels */
            QLabel {
                font: 13px 'Arial';
                color: #333;
            }

            /* Line Edit */
            QLineEdit {
                font: 13px 'Arial';
                border-radius: 5px;
                padding: 6px;
                border: 1px solid #bbb;
                background-color: #fff;
            }

            /* Text Edit */
            QTextEdit {
                font: 13px 'Arial';
                border-radius: 5px;
                border: 1px solid #bbb;
                background-color: #fff;
            }

            /* Push Buttons */
            QPushButton {
                font: 13px 'Arial';
                border-radius: 5px;
                padding: 6px 14px;
                background-color: #2196F3;
                color: white;
                border: none;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QPushButton:disabled {
                background-color: #9e9e9e;
                color: #f0f0f0;
            }

            /* Check Box */
            QCheckBox {
                font: 13px 'Arial';
                color: #333;
            }

            /* Combo Box */
            QComboBox {
                font: 13px 'Arial';
                border-radius: 5px;
                padding: 4px;
                border: 1px solid #bbb;
                background-color: #fff;
            }
        """)

    def fetch_transcript(self):
        url = self.url_input.text().strip()
        if not url:
            QMessageBox.warning(self, "Input Error", "Please enter a YouTube URL.")
            return

        video_id = extract_video_id(url) or url
        self.status_label.setText(f"Fetching transcript for video ID: {video_id}...")
        self.fetch_button.setEnabled(False)
        self.transcript_display.clear()
        self.thumbnail_label.clear()

        # Load video thumbnail if available
        thumbnail_url = f"https://img.youtube.com/vi/{video_id}/0.jpg"
        try:
            data = urllib.request.urlopen(thumbnail_url).read()
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            self.thumbnail_label.setPixmap(pixmap.scaled(320, 180, Qt.KeepAspectRatio))
        except Exception:
            # Thumbnail is optional; ignore errors if not available
            pass

        language = self.language_combo.currentText()
        # Start background thread to fetch transcript
        self.worker = TranscriptFetcher(video_id, language)
        self.worker.transcript_fetched.connect(self.on_transcript_fetched)
        self.worker.error_occurred.connect(self.on_error)
        self.worker.start()

    def on_transcript_fetched(self, transcript):
        self.transcript = transcript
        self.transcript_display.setPlainText(transcript)
        word_count = len(transcript.split())
        self.status_label.setText(f"Transcript retrieved. Word count: {word_count}")
        self.fetch_button.setEnabled(True)

    def on_error(self, error_message):
        QMessageBox.critical(self, "Error Fetching Transcript", error_message)
        self.status_label.setText("Error fetching transcript.")
        self.fetch_button.setEnabled(True)

    def save_transcript(self):
        if not self.transcript:
            QMessageBox.warning(self, "No Transcript", "There is no transcript to save.")
            return
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save Transcript", "", "Text Files (*.txt);;All Files (*)", options=options
        )
        if filename:
            try:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(self.transcript)
                self.status_label.setText(f"Transcript saved to {filename}")
            except Exception as e:
                QMessageBox.critical(self, "Save Error", str(e))
                self.status_label.setText("Error saving transcript.")

    def toggle_theme(self, state):
        """
        Switches between light and dark themes by applying custom palettes.
        """
        if state == Qt.Checked:
            # Define dark palette
            dark_palette = QPalette()
            dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
            dark_palette.setColor(QPalette.WindowText, Qt.white)
            dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
            dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
            dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
            dark_palette.setColor(QPalette.ToolTipText, Qt.white)
            dark_palette.setColor(QPalette.Text, Qt.white)
            dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
            dark_palette.setColor(QPalette.ButtonText, Qt.white)
            dark_palette.setColor(QPalette.BrightText, Qt.red)
            dark_palette.setColor(QPalette.Highlight, QColor(142, 45, 197))
            dark_palette.setColor(QPalette.HighlightedText, Qt.black)

            QApplication.instance().setPalette(dark_palette)
        else:
            # Define light palette
            light_palette = QPalette()
            light_palette.setColor(QPalette.Window, Qt.white)
            light_palette.setColor(QPalette.WindowText, Qt.black)
            light_palette.setColor(QPalette.Base, Qt.white)
            light_palette.setColor(QPalette.AlternateBase, QColor(240, 240, 240))
            light_palette.setColor(QPalette.ToolTipBase, Qt.white)
            light_palette.setColor(QPalette.ToolTipText, Qt.black)
            light_palette.setColor(QPalette.Text, Qt.black)
            light_palette.setColor(QPalette.Button, QColor(240, 240, 240))
            light_palette.setColor(QPalette.ButtonText, Qt.black)
            light_palette.setColor(QPalette.BrightText, Qt.red)
            light_palette.setColor(QPalette.Highlight, QColor(0, 120, 215))
            light_palette.setColor(QPalette.HighlightedText, Qt.white)

            QApplication.instance().setPalette(light_palette)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Use the modern Fusion style
    app.setStyle(QStyleFactory.create("Fusion"))

    # Apply a light palette by default
    light_palette = QPalette()
    light_palette.setColor(QPalette.Window, Qt.white)
    light_palette.setColor(QPalette.WindowText, Qt.black)
    light_palette.setColor(QPalette.Base, Qt.white)
    light_palette.setColor(QPalette.AlternateBase, QColor(240, 240, 240))
    light_palette.setColor(QPalette.ToolTipBase, Qt.white)
    light_palette.setColor(QPalette.ToolTipText, Qt.black)
    light_palette.setColor(QPalette.Text, Qt.black)
    light_palette.setColor(QPalette.Button, QColor(240, 240, 240))
    light_palette.setColor(QPalette.ButtonText, Qt.black)
    light_palette.setColor(QPalette.BrightText, Qt.red)
    light_palette.setColor(QPalette.Highlight, QColor(0, 120, 215))
    light_palette.setColor(QPalette.HighlightedText, Qt.white)

    app.setPalette(light_palette)

    window = MainWindow()
    window.show()
    sys.exit(app.exec_())