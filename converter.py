from PIL import Image, ImageOps, ImageFilter
import os


class Converter:
    def __init__(self, directory, destination, fileName, sizex, sizey, format, rotate, resizemethod):
        self.directory = directory
        self.destination = destination
        self.fileName = fileName
        self.sizex = sizex
        self.sizey = sizey
        self.format = format
        self.rotate = rotate
        self.resizemethod = resizemethod

    def convertPhoto(self):
        self.im = Image.open(self.directory + '/' + self.fileName)

        if (self.format == 'Orginal'):
            self.format = self.im.format
        else:
            if (self.im.format == 'JPEG'):
                tmp = 'jpg'
            elif (self.im.format == 'PNG'):
                tmp = 'png'
            elif (self.im.format == 'BMP'):
                tmp = 'bmp'
            self.fileName = self.fileName.lower()
            self.fileName = self.fileName.replace(tmp, self.format.lower())

        self.checkSize()



        self.checkexistname()
        self.im.rotate(self.rotate).save(self.destination + '/' + self.fileName, self.format)


    def checkSize(self):
        if (self.sizex != 0):
            if (self.resizemethod == 'Normal'):
                self.im = self.im.resize((self.sizex, self.sizey))
            elif (self.resizemethod == 'Thumbnail'):
                self.im.thumbnail((self.sizex, self.sizey))




    def checkexistname(self):
        while (True):
            if (os.path.isfile(self.destination + '/' + self.fileName)):
                self.fileName = "_" + self.fileName
            else:
                break


class ConventerMoreOptions(Converter):
    def __init__(self, directory, destination, fileName, sizex, sizey, format, rotate, resizemethod, moreParameters):
        self.directory = directory
        self.destination = destination
        self.fileName = fileName
        self.sizex = sizex
        self.sizey = sizey
        self.format = format
        self.rotate = rotate
        self.resizemethod = resizemethod
        self.moreParameters = moreParameters

    def convertPhoto(self):
        self.im = Image.open(self.directory + '/' + self.fileName)
        if (self.format == 'Orginal'):
            self.format = self.im.format
        else:
            if (self.im.format == 'JPEG'):
                tmp = 'jpg'
            elif (self.im.format == 'PNG'):
                tmp = 'png'
            elif (self.im.format == 'BMP'):
                tmp = 'bmp'
            self.fileName = self.fileName.lower()
            self.fileName = self.fileName.replace(tmp, self.format.lower())

        self.checkSize()
        self.checkexistname()
        self.changeMoreOptions()
        self.im.rotate(self.rotate).save(self.destination + '/' + self.fileName, self.format)

    def changeMoreOptions(self):
        if (self.moreParameters[0] == 1):
            self.im = ImageOps.grayscale(self.im)
        if ((self.moreParameters[1] == 1)):
            self.im = self.im.filter(ImageFilter.BLUR)
        if ((self.moreParameters[2] == 1)):
            self.im = self.im.filter(ImageFilter.CONTOUR)
        if ((self.moreParameters[3] == 1)):
            self.im = self.im.filter(ImageFilter.DETAIL)
        if ((self.moreParameters[4] == 1)):
            self.im = self.im.filter(ImageFilter.EDGE_ENHANCE)
        if ((self.moreParameters[5] == 1)):
            self.im = self.im.filter(ImageFilter.EDGE_ENHANCE_MORE)
        if ((self.moreParameters[6] == 1)):
            self.im = self.im.filter(ImageFilter.EMBOSS)
        if ((self.moreParameters[7] == 1)):
            self.im = self.im.filter(ImageFilter.FIND_EDGES)
        if ((self.moreParameters[8] == 1)):
            self.im = self.im.filter(ImageFilter.SMOOTH)
        if ((self.moreParameters[9] == 1)):
            self.im = self.im.filter(ImageFilter.SMOOTH_MORE)
        if ((self.moreParameters[10] == 1)):
            self.im = self.im.filter(ImageFilter.SHARPEN)
