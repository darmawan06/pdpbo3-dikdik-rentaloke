# Saya Dikdik Darmawan mengerjakan TP3 dalam mata kuliah DPBO untuk keberkahanya maka saya tidak melakukan kecurangan seperti yang telah di spesifikasikan. Aamiin.

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
from PackageClass import ClassFrameKiri as cfki
from PackageClass import ClassFrameKanan as cfka

class Main(Frame):
	def __init__(self,parent):
		Frame.__init__(self)
		self.FrameKiri = cfki.FrameKiri(parent,DataRental).pack(side=LEFT)
		self.FrameKanan = cfka.FrameKanan(parent,DataRental).pack(side=RIGHT)

if __name__ == '__main__':
	DataRental = []
	root = Tk(className=" TP3 PBO")
	Canvas(root,background="blue",width=640,height=20).pack(side=TOP)
	Canvas(root,background="Silver",width=20,height=450).pack(side=LEFT)
	Canvas(root,background="Silver",width=20,height=450).pack(side=RIGHT)
	Canvas(root,background="blue",width=640,height=20).pack(side=BOTTOM)
	Main(root)
	mainloop()