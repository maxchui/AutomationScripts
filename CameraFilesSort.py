import logging
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
        os.mkdir(f'{base_folder_path}/logs')
    except Exception as e:
        logging.exception("message")
    finally:
        # Initialise logging parameters
        LOG_FORMAT = '%(asctime)s %(levelname)s: %(message)s'
        logging.basicConfig(level=logging.DEBUG,
                            filename=f'{base_folder_path}/logs/CameraFilesSort_{datetime.now().strftime("%d-%m-%Y_%H-%M-%S")}.log',
                            filemode='w', format=LOG_FORMAT)
        logging.debug(f'Started log file in path = {base_folder_path}')

    file_entries = os.listdir(base_folder_path)

    # Terminate the program if the folder has nothing in it (the user is supposed to move the files into the folder first)
    if len(file_entries) == 0:
        logging.error("The folder is empty. Terminating...")
        quit()

    # Create the sub-folders to store the files with the same file extension
    for i in CAMERA_FOLDER_NAME:
        if i not in file_entries:
            try:
                os.mkdir(base_folder_path + '/' + i)
                logging.debug(f'Folder {i} does not exist, creating directory {i}')
            except:
                logging.exception("message")

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
                    logging.debug(f'Moving file {entry} from {source_address} to {destination_address}')
                except:
                    logging.exception("message")
            else:
                logging.error(f'Extension {file_extension} does not exist in the mapping table (entry={entry})')

    logging.info("Terminating program")