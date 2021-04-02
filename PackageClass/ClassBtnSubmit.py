from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
from PackageClass import DataRentalKendaraan as cd

class BtnSubmit():
	def __init__(self,frame,inputArea,locationPhoto,DataRental):
		self.frame = frame
		self.DataRental = DataRental
		self.inputArea = inputArea
		self.locationPhoto = locationPhoto
		self.Submit = Button(self.frame,
			text="Submit",
			width=30,
			height=1,
			bg="white",
			fg="black",command=self.addData).grid(column = 0)

	def addData(self):
		InputNoKTP = self.inputArea.GetValueNoKTP();
		InputNama = self.inputArea.GetValueNama();
		InputNamaKendaraan = self.inputArea.GetValueNamaKendaraan();
		InputJenisKendaraan = self.inputArea.GetValueJenisKendaraan();
		InputAksesoris = self.inputArea.GetValueAksesoris();
		InputWarna = self.inputArea.GetValueWarna();
		if(InputNoKTP == "" or InputNama == "" or InputNamaKendaraan == "" or InputJenisKendaraan == "" or len(InputAksesoris) == 0 or InputWarna == ""):
			response = messagebox.showwarning("Infomasi", "Field Input Ada Yang Kosong")
			Label(self.frame,text=response)
		else:
			InputLocationPhoto = self.locationPhoto.GetValue();
			self.DataRental.append(cd.DataRentalKendaraan(InputNoKTP,InputNama,InputNamaKendaraan,InputJenisKendaraan,InputAksesoris,InputWarna,InputLocationPhoto))
			response = messagebox.showinfo("Infomasi", "Data Berhasil Dimasukan")
			Label(self.frame,text=response)
			self.inputArea.Draw(self.frame)
	pass