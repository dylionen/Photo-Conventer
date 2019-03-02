from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox


class ShowPhotos():
    def __init__(self, photosList, directory, amountPhotosValue):
        self.listbox = ''
        self.filesNames = photosList
        self.directory = directory
        self.amountPhotosValue = amountPhotosValue

    def delPhoto(self):
        if (len(self.filesNames) > 1):
            if (self.listbox.curselection() != ()):
                self.filesNames.remove(self.listbox.get(self.listbox.curselection()))
                self.insertPhotosToList()
                self.amountPhotosValue.set("Photos: " + str(len(self.filesNames)))
            else:
                messagebox.showinfo("Error", "Nie zaznaczono żadnego obrazu")
        else:
            messagebox.showinfo("Error", "Nie możesz usunąć ostatniego obrazu")

    def openWindowToShowPhotos(self):
        self.windowList = Toplevel()
        self.windowList.geometry("500x500")
        self.windowList.title("Pictures List")

        self.description = Label(self.windowList, text="Check your Pictures:").pack()
        self.listbox = Listbox(self.windowList, width=80, height=20)
        self.listbox.pack()
        self.listbox.place(x=2, y=30)
        self.insertPhotosToList()
        # body
        self.convert = tk.Button(self.windowList, text='Open', command=self.showPhotofromListPhotos)
        self.convert.pack()
        self.convert.place(x=0, y=430)
        self.convert.config(width=20, height=3)

        self.delPhoto = tk.Button(self.windowList, text='Delete',
                                  command=self.delPhoto)
        self.delPhoto.pack()
        self.delPhoto.config(width=20, height=3)
        self.delPhoto.place(x=349, y=430)

    def insertPhotosToList(self):
        self.listbox.delete(0, tk.END)
        for photo in self.filesNames:
            self.listbox.insert(END, photo)

    def empty(self):
        pass

    def showPhotofromListPhotos(self):
        photo = self.listbox.get(self.listbox.curselection())

        showPhotoWindow = Toplevel()
        showPhotoWindow.geometry("500x500")
        showPhotoWindow.title("IMG")

        image = Image.open(self.directory + '/' + photo)

        tmp = image
        tmp.thumbnail((490, 490))
        photo = ImageTk.PhotoImage(tmp)
        label = tk.Label(showPhotoWindow, image=photo)
        label.image = photo
        label.pack()
