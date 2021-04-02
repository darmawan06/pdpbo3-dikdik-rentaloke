from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
from PackageClass import ClassBtnSubmit as cbs
from PackageClass import ClassInputArea as ci
from PackageClass import ClassBtnOpenPhotoFile as cbopf
class FrameKiri(Frame):
    def __init__(self, parent,DataRental):
        Frame.__init__(self, parent)
        self.DataRental = DataRental
        self.InputArea = ci.InputArea(self)
        self.InputArea.Draw(self)
        self.locationPhoto = cbopf.BtnOpenPhotoFile(self)        
        cbs.BtnSubmit(self,self.InputArea,self.locationPhoto,self.DataRental)
    pass