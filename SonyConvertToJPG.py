import os
import platform
import time
import subprocess
from tkinter import *
from tkinter import messagebox

from showinfm import show_in_file_manager

import pyautogui
import win32gui

def main(base_folder_path):
    root = Tk()
    root.withdraw()

    # Get the OS version
    os_version = platform.system()

    if os_version == "Windows":
        windows(base_folder_path)
    elif os_version == "Darwin":
        mac(base_folder_path)
    else:
        # Show tk prompt that the OS is not supported
        messagebox.showerror("Error", "OS not supported")
        quit()


def windows(base_folder_path):
    # subprocess.Popen(['C:\Program Files\Sony\Imaging Edge\Viewer.exe'])
    # time.sleep(5)

    # # Maximise the window
    # pyautogui.hotkey('win', 'up')

    # Open file explorer to the source folder then drag n drop that folder into the viewer's right hand side window
    # show_in_file_manager(path_or_uri=base_folder_path, open_not_select_directory=False)
    # time.sleep(2)
    # pyautogui.hotkey('win', 'up')
    # pyautogui.press('enter')
    # move the cursor to the selected folder in file explorer
    
    handle = win32gui.FindWindow(None, "Viewer")
    subHandle = win32gui.FindWindowEx(handle,0,None,None)
    menuitemhandle = win32gui.GetMenuIte
    print(subHandle)

    # messagebox.showerror("Error", "OS not supported")


def mac(base_folder_path):
    print("do something useful here")


if __name__ == '__main__':
    main(r"C:\Users\max\OneDrive - HKUST Connect\Photos & Videos\Sony A7 IV\2023-01-25\RAW")
