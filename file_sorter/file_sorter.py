import os
import shutil
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QFileDialog,
    QTextEdit, QLabel, QProgressBar
)
from PyQt5.QtCore import QThread, pyqtSignal

# Define your file types mapping
FILE_TYPES = {
    "PDFs": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "ZIP_Files": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".bat"],
    "Documents": [".doc", ".docx", ".txt", ".odt", ".rtf"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
}

# Utility functions for file operations
def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

def get_unique_destination(destination_folder, filename):
    base, ext = os.path.splitext(filename)
    counter = 1
    new_filename = filename
    dest_path = os.path.join(destination_folder, new_filename)
    while os.path.exists(dest_path):
        new_filename = f"{base}{counter}{ext}"
        dest_path = os.path.join(destination_folder, new_filename)
        counter += 1
    return dest_path

def move_file(file_path, destination_folder):
    create_folder(destination_folder)
    filename = os.path.basename(file_path)
    destination = get_unique_destination(destination_folder, filename)
    try:
        shutil.move(file_path, destination)
    except Exception as e:
        # You might want to handle errors or log them appropriately
        pass

# Worker thread for sorting files so the GUI remains responsive
class SortWorker(QThread):
    log_signal = pyqtSignal(str)
    progress_signal = pyqtSignal(int)
    finished_signal = pyqtSignal()

    def __init__(self, folder):
        super().__init__()
        self.folder = folder

    def run(self):
        # Get list of non-directory files in the selected folder
        files = [item for item in os.listdir(self.folder)
                 if os.path.isfile(os.path.join(self.folder, item))]
        total_files = len(files)
        if total_files == 0:
            self.log_signal.emit("No files found in the selected folder.")
            self.finished_signal.emit()
            return

        count = 0
        for item in files:
            item_path = os.path.join(self.folder, item)
            _, ext = os.path.splitext(item)
            ext = ext.lower()
            sorted_file = False
            for folder_name, extensions in FILE_TYPES.items():
                if ext in extensions:
                    destination = os.path.join(self.folder, folder_name)
                    move_file(item_path, destination)
                    self.log_signal.emit(f"Moved '{item}' to '{folder_name}' folder.")
                    sorted_file = True
                    break
            if not sorted_file:
                destination = os.path.join(self.folder, "Others")
                move_file(item_path, destination)
                self.log_signal.emit(f"Moved '{item}' to 'Others' folder.")
            count += 1
            progress = int((count / total_files) * 100)
            self.progress_signal.emit(progress)
        self.log_signal.emit("Sorting completed!")
        self.finished_signal.emit()

# Main GUI window using PyQt5
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Downloads Auto Sorter")
        self.resize(600, 400)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Folder selection
        self.folder_label = QLabel("Folder to sort:")
        self.layout.addWidget(self.folder_label)

        self.folder_line_edit = QLineEdit()
        self.folder_line_edit.setText(os.path.expanduser("~/Downloads"))
        self.layout.addWidget(self.folder_line_edit)

        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.browse_folder)
        self.layout.addWidget(self.browse_button)

        # Sorting control
        self.sort_button = QPushButton("Start Sorting")
        self.sort_button.clicked.connect(self.start_sorting)
        self.layout.addWidget(self.sort_button)

        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.layout.addWidget(self.progress_bar)

        # Log window
        self.log_text_edit = QTextEdit()
        self.log_text_edit.setReadOnly(True)
        self.layout.addWidget(self.log_text_edit)

        self.worker = None

    def browse_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder", os.path.expanduser("~"))
        if folder:
            self.folder_line_edit.setText(folder)

    def start_sorting(self):
        folder = self.folder_line_edit.text().strip()
        if not folder or not os.path.exists(folder):
            self.log("Invalid folder selected.")
            return

        # Disable the sort button while sorting is in progress
        self.sort_button.setEnabled(False)
        self.log("Starting sorting...")
        self.worker = SortWorker(folder)
        self.worker.log_signal.connect(self.log)
        self.worker.progress_signal.connect(self.update_progress)
        self.worker.finished_signal.connect(self.sorting_finished)
        self.worker.start()

    def log(self, message):
        self.log_text_edit.append(message)

    def update_progress(self, value):
        self.progress_bar.setValue(value)

    def sorting_finished(self):
        self.sort_button.setEnabled(True)
        self.log("Sorting process finished.")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
