import logging.config
import os
import shutil
import tkinter as tk
from datetime import datetime
from tkinter import filedialog

from Constants import CAMERA_FILE_TO_FOLDER_MAPPING
from Constants import CAMERA_FOLDER_NAME


def main():
    root = tk.Tk()
    # Hide the root window
    root.withdraw()

    # Ask the user where to save the log files
    base_folder_path = ''
    try:
        base_folder_path = filedialog.askdirectory(
            title='Please select the folder where you have placed the image files')

        if not os.path.exists(base_folder_path + "/logs"):
            logging.debug(f'Log folder does not exist, creating log directory')
            os.mkdir(f'{base_folder_path}/logs')
    except Exception as e:
        logging.exception("message")

    # Initialise logging parameters
    LOG_FORMAT = '%(asctime)s %(levelname)s: %(message)s'
    logging.basicConfig(level=logging.DEBUG,
                        handlers=[logging.FileHandler(
                            f'{base_folder_path}/Logs/CameraFilesSort_{datetime.now().strftime("%d-%m-%Y_%H-%M-%S")}.log'),
                            logging.StreamHandler()],
                        format=LOG_FORMAT, force=True)
    logger = logging.getLogger(__name__)
    print(logger)
    logger.debug(f'Started log file in path = {base_folder_path}')

    file_entries = os.listdir(base_folder_path)

    # Terminate the program if the folder has nothing in it (the user is supposed to move the files into the folder first)
    if len(file_entries) == 0:
        logger.error("The folder is empty. Terminating...")
        quit()

    # Create the sub-folders to store the files with the same file extension
    for i in CAMERA_FOLDER_NAME:
        if i not in file_entries:
            try:
                os.mkdir(base_folder_path + '/' + i)
                logger.debug(f'Folder {i} does not exist, creating directory {i}')
            except:
                logger.exception("message")

    # Time to move dem files :D
    for entry in os.listdir(base_folder_path):
        # Ignore system files
        if entry == '.DS_Store':
            continue

        if os.path.isfile(os.path.join(base_folder_path, entry)):
            file_extension = os.path.splitext(os.path.join(base_folder_path, entry))[1].strip(".")
            if file_extension.strip(".") in CAMERA_FILE_TO_FOLDER_MAPPING:
                try:
                    source_address = os.path.join(base_folder_path, entry)
                    destination_address = os.path.join(base_folder_path, CAMERA_FILE_TO_FOLDER_MAPPING[file_extension])
                    shutil.move(source_address, destination_address)
                    logger.debug(f'Moving file {entry} from {source_address} to {destination_address}')
                except:
                    logger.exception("message")
            else:
                logger.error(f'Extension {file_extension} does not exist in the mapping table (entry={entry})')

    logger.info("Terminating program")
