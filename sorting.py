import os
import shutil
from concurrent.futures import ThreadPoolExecutor

def process_folder(path):
    files = os.listdir(path)
    files_by_extension = {}
    for file in files:
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            _, extension = os.path.splitext(file)
            if extension not in files_by_extension:
                files_by_extension[extension] = []
            files_by_extension[extension].append(file_path)

    with ThreadPoolExecutor() as executor:
        for extension, file_paths in files_by_extension.items():
            for file_path in file_paths:
                executor.submit(move_file, file_path, extension)

    remove_empty_folders(path)  # Removing empty folders after file processing

def move_file(file_path, extension):
    destination_folder = os.path.join("Мотлох", extension.strip('.'))
    os.makedirs(destination_folder, exist_ok=True)
    destination_path = os.path.join(destination_folder, os.path.basename(file_path))
    shutil.move(file_path, destination_path)

def remove_empty_folders(path):
    for root, dirs, _ in os.walk(path, topdown=False):
        for directory in dirs:
            folder_path = os.path.join(root, directory)
            if not os.listdir(folder_path):  # Check if folder is empty
                os.rmdir(folder_path)

def process_directory(path):
    with ThreadPoolExecutor() as executor:
        for root, _, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                _, extension = os.path.splitext(file)
                executor.submit(move_file, file_path, extension)

    remove_empty_folders(path)  # Removing empty folders after file processing

if __name__ == "__main__":
    folder_path = input("Enter the path to the 'Мотлох' folder: ")
    process_directory(folder_path)
