import logging
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

# Import constants from your separate file
from Constants import CAMERA_FILE_TO_FOLDER_MAPPING, CAMERA_FOLDER_NAME

def setup_logging(base_folder):
    log_directory = base_folder / "logs"
    log_directory.mkdir(exist_ok=True)
    log_file = log_directory / f"CameraFilesSort_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.log"
    logging.basicConfig(level=logging.DEBUG,
                        handlers=[logging.FileHandler(str(log_file)),
                                  logging.StreamHandler()],
                        format='%(asctime)s %(levelname)s: %(message)s', force=True)
    return logging.getLogger(__name__)

def create_folder_if_not_exists(folder):
    if not folder.exists():
        folder.mkdir()
        logging.debug(f'Folder {folder} created.')

def handle_files(base_folder):
    file_entries = list(base_folder.iterdir())
    if not file_entries:
        logging.error("The folder is empty. Terminating...")
        quit()
    
    # Create necessary folders based on existing file types
    detected_extensions = {entry.suffix[1:].upper() for entry in file_entries if entry.is_file()}
    for extension in detected_extensions:
        if extension in CAMERA_FILE_TO_FOLDER_MAPPING:
            folder_name = CAMERA_FILE_TO_FOLDER_MAPPING[extension]
            if folder_name not in ['MP4', 'JPG']:  # Skip initial creation for MP4 and JPG
                folder = base_folder / folder_name
                create_folder_if_not_exists(folder)

    # Move files
    for entry in file_entries:
        if entry.is_file():
            file_extension = entry.suffix[1:].upper()
            if file_extension in CAMERA_FILE_TO_FOLDER_MAPPING:
                destination_folder = base_folder / CAMERA_FILE_TO_FOLDER_MAPPING[file_extension]
                create_folder_if_not_exists(destination_folder)  # Create the folder here if not exists
                try:
                    shutil.move(str(entry), str(destination_folder))
                    logging.debug(f'Moving file {entry} to {destination_folder}')
                except Exception as e:
                    logging.error(f'Failed to move file {entry}: {str(e)}')
            else:
                logging.error(f'Extension {file_extension} is not recognized (file={entry})')

def main():
    root = tk.Tk()
    root.withdraw()
    base_folder_path = filedialog.askdirectory(title='Select the folder for sorting files')
    if not base_folder_path:
        logging.error("No folder selected. Exiting...")
        return
    base_folder = Path(base_folder_path)
    logger = setup_logging(base_folder)
    handle_files(base_folder)
    logger.info("Termination of program.")
