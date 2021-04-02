from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

class LabelNamaProgram():
	def __init__(self,frame):
		self.frame = frame
		LabelAplication = Label(self.frame,
			text="Application",
			font=("",20,"bold"),
			foreground="blue",
			width=12,
			anchor="w").grid(column = 0)
		LabelName = Label(self.frame,
			text="Rental OKE",
			font=("",20,"bold"),
			anchor="w",
			foreground="blue",
			width=12).grid(column = 0)
		LabelDeskripsi = Label(self.frame,
			text="Rental OKE adalah sebuah aplikasi\n yang mencatat pelanggan yang\n meminjam kendaraan\n",
			font=("bold"),
			anchor="w",
			foreground="black").grid(column = 0)