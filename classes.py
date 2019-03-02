from tkinter import *
import tkinter as tk
from tkinter import filedialog
import os
from listfiles import FilesOperations
from showphotos import ShowPhotos
from os import *
from tkinter import messagebox
import fnmatch
from PIL import Image, ImageTk


class MainWindow:
    def __init__(self):
        self.destTrue = False
        self.dirTrue = False
        self.amountPhotosValue = None
        self.showMainWindow()

    def showMainWindow(self):
        self.window = tk.Tk()
        self.window.geometry("500x500")
        self.window.title("Photo Converter 1.0")
        self.window.resizable(0, 0)
        self.showDirectoryOptions()
        tk.mainloop()

    def showDirectoryOptions(self):
        self.description = tk.Label(self.window, text="From:")
        self.description.pack()
        self.description.place(x=0, y=0)

        self.textFrom = tk.StringVar()
        self.labelFrom = tk.Label(self.window, textvariable=self.textFrom, padx=100, pady=0)
        self.labelFrom.pack()
        self.labelFrom.place(x=20, y=20)
        self.textFrom.set("Brak folderu")
        self.labelFrom.configure(fg="red")

        self.directory = tk.Button(self.window, text='Add Directory', command=self.addFolderDirectory)

        self.directory.pack()
        self.directory.place(x=0, y=20)

    def showDestinationOptions(self):
        self.description2 = tk.Label(self.window, text="To:")
        self.description2.pack()
        self.description2.place(x=0, y=50)

        self.textTo = tk.StringVar()
        self.labelTo = tk.Label(self.window, textvariable=self.textTo, padx=100, pady=0)
        self.labelTo.pack()
        self.labelTo.place(x=20, y=70)
        self.textTo.set("Brak folderu")
        self.labelTo.configure(fg="red")

        self.destination = tk.Button(self.window, text='Add Destination', command=self.addFolderSource)
        self.destination.pack()
        self.destination.place(x=0, y=70)

    def addFolderDirectory(self):
        tmp = filedialog.askdirectory()
        self.directory = tmp
        self.dirTrue = os.path.exists(tmp)
        if (self.dirTrue == True):
            self.filesoperations = FilesOperations(tmp)
            if (len(self.filesoperations.filesNames) != 0):
                self.showDestinationOptions()
                self.showRefreshButton()
                self.folderCheck(tmp, self.textFrom, self.labelFrom)
                self.showInformationAboutAmountPhotos()
            else:
                messagebox.showinfo("Error", "W folderze nie znajdują się żadne obrazy")

    def showRefreshButton(self):
        self.refreshButton = tk.Button(self.window, text='Refresh', command=self.refreshPictures, bg='yellow')
        self.refreshButton.pack()
        self.refreshButton.place(x=220, y=470)

    def refreshPictures(self):
        self.filesoperations.photoFiles(self.directory)
        self.amountPhotosValue.set("Photos: " + str(len(self.filesoperations.filesNames)))

    def showInformationAboutAmountPhotos(self):
        self.amountPhotosValue = tk.StringVar()
        self.amountPhotos = tk.Label(self.window, textvariable=self.amountPhotosValue)
        self.amountPhotos.pack()
        self.amountPhotos.place(x=220, y=450)
        self.amountPhotosValue.set("Photos: " + str(len(self.filesoperations.filesNames)))

    def addFolderSource(self):
        tmp = filedialog.askdirectory()
        self.destination = tmp
        self.destTrue = os.path.exists(tmp)
        if (self.destTrue == True):
            if (self.destination != self.directory):
                self.filesoperations.addFolderSource(tmp)
                self.folderCheck(tmp, self.textTo, self.labelTo)
            else:
                messagebox.showinfo("Error", "Foldery nie mogą być takie same")

    def folderCheck(self, folder, tresc, label):
        if (os.path.exists(folder) == True):
            tresc.set(folder)
            label.configure(fg="green")
        self.showConvertOptions()

    def showConvertOptions(self):
        if (self.dirTrue == True and self.destTrue == True):
            self.convert = tk.Button(self.window, text='Convert', command=self.startConvert)
            self.convert.pack()
            self.convert.place(x=0, y=430)
            self.convert.config(width=20, height=3)
            self.showListPhotosOption()
            self.showPhotoRotateOptions()
            self.showFileFormatOptions()
            self.showPhotosize()
            self.showMoreOptions()

    def showListPhotosOption(self):
        self.listPhotosClass = ShowPhotos(self.filesoperations.filesNames, self.filesoperations.directory,
                                          self.amountPhotosValue)
        self.listPhotos = tk.Button(self.window, text='Show photos list',
                                    command=self.listPhotosClass.openWindowToShowPhotos)
        self.listPhotos.pack()
        self.listPhotos.config(width=20, height=3)
        self.listPhotos.place(x=349, y=430)

    def showPhotoRotateOptions(self):
        self.rotatePhoto = tk.StringVar()
        self.rotate = tk.Label(self.window, text="Rotate (degrees):")
        self.rotate.pack()
        self.rotate.place(x=0, y=130)
        self.rb_one = tk.Radiobutton(self.window, variable=self.rotatePhoto,
                                     value="0", text="0")
        self.rb_two = tk.Radiobutton(self.window, variable=self.rotatePhoto,
                                     value="90", text="90")
        self.rb_three = tk.Radiobutton(self.window, variable=self.rotatePhoto,
                                       value="180", text="180")
        self.rb_four = tk.Radiobutton(self.window, variable=self.rotatePhoto,
                                      value="270", text="270")
        self.rotatePhoto.set("0")
        self.rb_one.pack()
        self.rb_one.place(x=100, y=130)
        self.rb_two.pack()
        self.rb_two.place(x=150, y=130)
        self.rb_three.pack()
        self.rb_three.place(x=200, y=130)
        self.rb_four.pack()
        self.rb_four.place(x=250, y=130)

    def showFileFormatOptions(self):
        self.formatPhoto = tk.StringVar()
        self.format = tk.Label(self.window, text="File format:")
        self.format.pack()
        self.format.place(x=0, y=160)
        self.file_one = tk.Radiobutton(self.window, variable=self.formatPhoto,
                                       value="Orginal", text="Orginal")
        self.file_two = tk.Radiobutton(self.window, variable=self.formatPhoto,
                                       value="JPEG", text="JPEG")
        self.file_three = tk.Radiobutton(self.window, variable=self.formatPhoto,
                                         value="PNG", text="PNG")
        self.file_four = tk.Radiobutton(self.window, variable=self.formatPhoto,
                                        value="BMP", text="BMP")
        self.formatPhoto.set("Orginal")
        self.file_one.pack()
        self.file_one.place(x=100, y=160)
        self.file_two.pack()
        self.file_two.place(x=170, y=160)
        self.file_three.pack()
        self.file_three.place(x=220, y=160)
        self.file_four.pack()
        self.file_four.place(x=270, y=160)

    def showPhotosize(self):
        self.orginalSize = tk.IntVar();
        self.sizeCheck = tk.Checkbutton(self.window,
                                        text='Orginal size',
                                        variable=self.orginalSize,
                                        command=self.activeSizeOutput)
        self.sizeCheck.pack()
        self.sizeCheck.place(x=0, y=100)
        self.showSizeInput()

    def showSizeInput(self):
        self.photoX = tk.Label(self.window, text="X:")
        self.photoX.pack()
        self.photoX.place(x=87, y=100)
        self.widthPhoto = Entry(self.window, width=4)
        self.widthPhoto.pack()
        self.widthPhoto.place(x=100, y=100)

        self.photoY = tk.Label(self.window, text="Y:")
        self.photoY.pack()
        self.photoY.place(x=132, y=100)
        self.heightPhoto = Entry(self.window, width=4)
        self.heightPhoto.pack()
        self.heightPhoto.place(x=145, y=100)

        self.resizemethodValue = tk.StringVar()
        self.resizemethod = tk.Label(self.window, text="File format:")
        self.resizemethod.pack()
        self.resizemethod.place(x=180, y=100)
        self.resizemethod_one = tk.Radiobutton(self.window, variable=self.resizemethodValue,
                                               value="Thumbnail", text="Thumbnail")
        self.resizemethod_two = tk.Radiobutton(self.window, variable=self.resizemethodValue,
                                               value="Normal", text="Normal")

        self.resizemethodValue.set("Normal")
        self.resizemethod_one.pack()
        self.resizemethod_one.place(x=250, y=100)
        self.resizemethod_two.pack()
        self.resizemethod_two.place(x=330, y=100)

    def activeSizeOutput(self):
        if (self.orginalSize.get() == 1):
            self.widthPhoto.config(state=DISABLED)
            self.heightPhoto.config(state=DISABLED)
            self.resizemethod.config(state=DISABLED)
            self.resizemethod_one.config(state=DISABLED)
            self.resizemethod_two.config(state=DISABLED)
        else:
            self.widthPhoto.config(state=NORMAL)
            self.heightPhoto.config(state=NORMAL)
            self.resizemethod.config(state=NORMAL)
            self.resizemethod_one.config(state=NORMAL)
            self.resizemethod_two.config(state=NORMAL)

    def startConvert(self):
        try:
            sizex = 0
            sizey = 0

            if (self.orginalSize.get() == 0):
                sizex = int(self.widthPhoto.get())
                sizey = int(self.heightPhoto.get())
            format = self.formatPhoto.get();
            rotate = int(self.rotatePhoto.get())
            resizemethod = self.resizemethodValue.get()

            self.filesoperations.convert(sizex, sizey, format, rotate, resizemethod, self.getValuesFromMoreOptions())
        except ValueError as verr:
            messagebox.showinfo("Error", "Wprowadź poprawne liczby")

    def showMoreOptions(self):
        self.moreoptionsVal = tk.IntVar();
        self.moreoptions = tk.Checkbutton(self.window,
                                          text='More options',
                                          variable=self.moreoptionsVal,
                                          command=self.activeMoreOptions)
        self.moreoptions.pack()
        self.moreoptions.place(x=130, y=190)

    def getValuesFromMoreOptions(self):
        if (self.moreoptionsVal.get() == 1):
            moreOptionsChecks = []
            moreOptionsChecks.append(self.grayscaleValue.get())
            moreOptionsChecks.append(self.blurValue.get())
            moreOptionsChecks.append(self.contourValue.get())
            moreOptionsChecks.append(self.detailValue.get())
            moreOptionsChecks.append(self.edgeenhanceValue.get())
            moreOptionsChecks.append(self.edgeenhancemoreValue.get())
            moreOptionsChecks.append(self.embossValue.get())
            moreOptionsChecks.append(self.smoothValue.get())
            moreOptionsChecks.append(self.smoothmoreValue.get())
            moreOptionsChecks.append(self.findedgesValue.get())
            moreOptionsChecks.append(self.sharpenValue.get())
            return moreOptionsChecks
        else:
            return None

    def activeMoreOptions(self):
        if (self.moreoptionsVal.get() == 1):
            # GrayScale
            self.grayscaleValue = tk.IntVar()
            self.grayscale = tk.Checkbutton(self.window,
                                            text='Gray Scale',
                                            variable=self.grayscaleValue)
            self.grayscale.pack()
            self.grayscale.place(x=0, y=220)

            # BLUR
            self.blurValue = tk.IntVar()
            self.blur = tk.Checkbutton(self.window,
                                       text='Blur',
                                       variable=self.blurValue)
            self.blur.pack()
            self.blur.place(x=0, y=240)

            # CONTOUR
            self.contourValue = tk.IntVar()
            self.contour = tk.Checkbutton(self.window,
                                          text='Contour',
                                          variable=self.contourValue)
            self.contour.pack()
            self.contour.place(x=0, y=260)

            # DETAIL
            self.detailValue = tk.IntVar()
            self.detail = tk.Checkbutton(self.window,
                                         text='Detail',
                                         variable=self.detailValue)
            self.detail.pack()
            self.detail.place(x=0, y=280)

            # EDGE_ENHANCE
            self.edgeenhanceValue = tk.IntVar()
            self.edgeenhance = tk.Checkbutton(self.window,
                                              text='Edge Enhance',
                                              variable=self.edgeenhanceValue)
            self.edgeenhance.pack()
            self.edgeenhance.place(x=0, y=300)

            # EDGE_ENHANCE_MORE
            self.edgeenhancemoreValue = tk.IntVar()
            self.edgeenhancemore = tk.Checkbutton(self.window,
                                                  text='Edge Enhance More',
                                                  variable=self.edgeenhancemoreValue)
            self.edgeenhancemore.pack()
            self.edgeenhancemore.place(x=240, y=220)

            # EMBOSS
            self.embossValue = tk.IntVar()
            self.emboss = tk.Checkbutton(self.window,
                                         text='Emboss',
                                         variable=self.embossValue)
            self.emboss.pack()
            self.emboss.place(x=240, y=240)
            # FIND_EDGES
            self.findedgesValue = tk.IntVar()
            self.findedges = tk.Checkbutton(self.window,
                                            text='Find Edges',
                                            variable=self.findedgesValue)
            self.findedges.pack()
            self.findedges.place(x=240, y=260)

            # SMOOTH
            self.smoothValue = tk.IntVar()
            self.smooth = tk.Checkbutton(self.window,
                                         text='Smooth',
                                         variable=self.smoothValue)
            self.smooth.pack()
            self.smooth.place(x=240, y=280)

            # SMOOTH_MORE
            self.smoothmoreValue = tk.IntVar()
            self.smoothmore = tk.Checkbutton(self.window,
                                             text='Smooth more',
                                             variable=self.smoothmoreValue)
            self.smoothmore.pack()
            self.smoothmore.place(x=240, y=300)

            # SHARPEN
            self.sharpenValue = tk.IntVar()
            self.sharpen = tk.Checkbutton(self.window,
                                          text='Sharpen',
                                          variable=self.sharpenValue)
            self.sharpen.pack()
            self.sharpen.place(x=120, y=320)


        else:
            self.grayscale.destroy()
            self.blur.destroy()
            self.contour.destroy()
            self.detail.destroy()
            self.edgeenhance.destroy()
            self.edgeenhancemore.destroy()
            self.emboss.destroy()
            self.smooth.destroy()
            self.smoothmore.destroy()
            self.findedges.destroy()
            self.sharpen.destroy()

    def empty(self):
        pass
