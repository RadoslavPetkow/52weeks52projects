import os
import shutil

FILE_TYPES = {
    "PDFs": [".pdf"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "ZIP_Files": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executables": [".exe", ".msi", ".bat"],
    "Documents": [".doc", ".docx", ".txt", ".odt", ".rtf"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
}

downloads_folder = os.path.expanduser("~/Downloads")

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
        print(f"Moved: {filename} -> {destination}")
    except Exception as e:
        print(f"Error moving {file_path}: {e}")

def auto_sort_downloads():
    for item in os.listdir(downloads_folder):
        item_path = os.path.join(downloads_folder, item)
        if os.path.isdir(item_path):
            continue
        _, ext = os.path.splitext(item)
        ext = ext.lower()
        sorted_file = False
        for folder_name, extensions in FILE_TYPES.items():
            if ext in extensions:
                destination = os.path.join(downloads_folder, folder_name)
                move_file(item_path, destination)
                sorted_file = True
                break
        if not sorted_file:
            destination = os.path.join(downloads_folder, "Others")
            move_file(item_path, destination)

if __name__ == "__main__":
    auto_sort_downloads()
