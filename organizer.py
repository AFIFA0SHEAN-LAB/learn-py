import os
import shutil

src_path = 'C:/Users/afifa/Downloads'
dst_path = 'C:/fileorganizer'

file_exts = {
    "Video" : (".mp4", ".mov"),
    "Audio" : (".mp3", ".wav"),
    "Image" : (".jpg", ".png", ".jpeg", ".jfif", ".webp", ".amv"),
    "Documents" : (".pdf", ".docx", ".doc", ".xlsx", ".pptx"),
    "Applications" : (".exe", ".msi", ".dmg"),
    "Archives" : (".zip", ".rar", ".7z", ".tar", ".gz")
}

for k in file_exts:
    target_folder = os.path.join(dst_path, k)
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    else:
        pass

detect_files = os.listdir(src_path)

for file in detect_files:
    src_file_path = os.path.join(src_path, file)

    if os.path.isdir(src_file_path):
        continue

    filelower = file.lower()

    for cat, ext in file_exts.items():
        if filelower.endswith(ext):
            sort_folder = os.path.join(dst_path, cat)
            shutil.move(src_file_path, sort_folder)
            print(f"Successfully moved {file} to {cat}.")
            break