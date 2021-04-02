from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
from PackageClass import ClassFrameKiri as cfk
from PackageClass import ClassLabelNamaProgram as clnp
from PackageClass import ClassBtnProses as cbp

class FrameKanan(Frame):
    def __init__(self, parent,DataRental):
        Frame.__init__(self, parent)
        self.DataRental = DataRental
        clnp.LabelNamaProgram(self)
        cbp.BtnProses(self,parent,self.DataRental)