import tkinter
from tkinter import filedialog
import os
from abc import ABC, abstractmethod

class Finder:
    @abstractmethod
    def find(self):
        self.root = tkinter.Tk()
        self.root.withdraw()
        self.root.overrideredirect(True)
        self.root.wm_attributes('-topmost', True)
        currdir = os.getcwd()
        tempdir = filedialog.askdirectory(parent=self.root, initialdir=currdir, title='Please select a folder')
        if len(tempdir) > 0:
            return tempdir
        return None
