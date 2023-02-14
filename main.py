import math

import CameraFilesSort
import tkinter as tk
from tkinter import *

import Constants


class Automator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.title('Automator')
        # Set the default size of the window to be 40% of the screenwidth/height
        self.geometry(f'{math.trunc(self.winfo_screenwidth() * 0.4)}x{math.trunc(self.winfo_screenheight() * 0.4)}')

        # Dropdown menu options initialisation
        variable = StringVar(self)
        variable.set(Constants.MAIN_MENU_OPTIONS_MAPPING[0])

        drop_menu = OptionMenu(self, variable, *Constants.MAIN_MENU_OPTIONS_MAPPING)
        drop_menu.pack()


if __name__ == '__main__':
    #app = Automator()
    # app.mainloop()
    CameraFilesSort.main()
