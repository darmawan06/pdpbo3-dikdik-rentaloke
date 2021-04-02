from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

class BtnOpenPhotoFile():
	def __init__(self,frame):
		self.frame = frame
		self.location = "null"
		self.ButtonOpenFile = Button(self.frame,
			text="Open Photo File",
			width=30,
			height=1,
			bg="white",
			fg="black",command= self.OpenFile).grid(column = 0)

	def OpenFile(self):
		name = filedialog.askopenfilename(initialdir = "/", title="Select a File", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
		self.location = name

	def GetValue(self):
		size=150,150
		if(self.location != "null"):
			photo = ImageTk.PhotoImage(Image.open(self.location).resize(size)) 
			return photo
		else:
			return "null"
	pass