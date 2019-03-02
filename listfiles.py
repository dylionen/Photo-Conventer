import fnmatch
import os
from converter import Converter, ConventerMoreOptions
from tkinter import *
import time


class FilesOperations():
    def __init__(self, directory):
        self.directory = directory
        self.filesNames = []
        self.photoFiles(self.directory)

    def addFolderSource(self, destination):
        self.destination = destination

    def photoFiles(self, directory):
        self.filesNames = []
        for file in os.listdir(self.directory):
            if fnmatch.fnmatch(file, '*.jpg') or fnmatch.fnmatch(file, '*.png') or fnmatch.fnmatch(file, '*.bmp'):
                self.filesNames.append(file)

    def openWindowLog(self):
        self.logList = Toplevel()
        self.logList.geometry("300x200")
        self.logList.title("Log")

        self.description = Label(self.logList, text="Log Files").pack()
        self.loglistbox = Listbox(self.logList, width=80, height=20)
        self.loglistbox.pack()
        self.loglistbox.place(x=2, y=30)

    def convert(self, sizex, sizey, format, rotate, resizemethod, moreList):
        self.openWindowLog()
        if (moreList == None):
            for photo in self.filesNames:
                tmp = Converter(self.directory, self.destination, photo, sizex, sizey, format, rotate, resizemethod)
                tmp.convertPhoto()
                self.loglistbox.insert(END, "Wykonano konawersję pliku " + photo)
                del tmp
        else:
            for photo in self.filesNames:
                tmp = ConventerMoreOptions(self.directory, self.destination, photo, sizex, sizey, format, rotate,
                                           resizemethod, moreList)
                tmp.convertPhoto()
                self.loglistbox.insert(END, "Wykonano konawersję pliku " + photo)
                del tmp
