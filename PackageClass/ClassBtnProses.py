from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

class BtnProses():
	def __init__(self,frame,root,DataRental):
		self.frame = frame
		self.root = root
		self.DataRental = DataRental
		self.ButtonSeeAllSubmissions = Button(self.frame,
			text="SEE ALL SUBMISSIONS",
			width=30,
			height=1,
			bg="white",
			fg="black",command=lambda:self.LihatData() ).grid(column = 0)
		self.ButtonClearSubmissions = Button(self.frame,
			text="CLEAR SUBMISSIONS",
			width=30,
			height=1,
			bg="white",
			fg="black",command=lambda:self.ClearData()).grid(column = 0)
		self.ButtonAbout = Button(self.frame,
			text="ABOUT",
			width=30,
			height=1,
			bg="white",
			fg="black",command=lambda:self.Keterangan()).grid(column = 0)
		barisBaru = Label(self.frame,
		text="\n\n\n").grid(column = 0)
		ButtonExit = Button(self.frame,
			text="EXIT",
			width=30,
			height=1,
			bg="white",
			fg="black",command=lambda:self.CloseProgram()).grid(column= 0)

	def LihatData(self):
		FrameData = Toplevel()
		Label(FrameData,text="No KTP",background="grey").grid(column=0,row=0)
		Label(FrameData,text="Nama",background="white").grid(column=1,row=0)
		Label(FrameData,text="NamaKendaraan",background="blue").grid(column=2,row=0)
		Label(FrameData,text="JenisKendaraan",background="yellow").grid(column=3,row=0)
		Label(FrameData,text="Aksesoris",background="red").grid(column=4,row=0)
		Label(FrameData,text="Warna",background="green").grid(column=5,row=0)
		Label(FrameData,text="Gambar Mobil",background="silver").grid(column=6,row=0)
		i = 1
		for data in self.DataRental:
			Label(FrameData,text=data.NoKTP).grid(column=0,row=i)
			Label(FrameData,text=data.Nama).grid(column=1,row=i)
			Label(FrameData,text=data.NamaKendaraan).grid(column=2,row=i)
			Label(FrameData,text=data.JenisKendaraan).grid(column=3,row=i)
			Label(FrameData,text=data.Aksesoris).grid(column=4,row=i)
			Label(FrameData,text=data.Warna).grid(column=5,row=i)
			if(data.Photo != 'null'):
				Label(FrameData,image=data.Photo).grid(column=6,row=i)
			else:
				Label(FrameData,text="Gambar Kosong").grid(column=6,row=i)
			i = i+1
			pass
		pass

	def ClearData(self):
		response = messagebox.askquestion("Peringatan", "Apakah Anda Serius Ingin Menghapus Data Ini ?")
		if(response == "yes"):
			self.DataRental.clear()
			response = messagebox.showinfo("Infomasi", "Data Berhasil Di Hapus")
		else:
			response = messagebox.showinfo("Infomasi", "Data Batal Di Hapus")

	def Keterangan(self):
		FrameKet = Toplevel()
		Label(FrameKet,text="Rental OKE",font=("",20,"bold"),anchor="w",foreground="blue",width=12).grid(column = 0)
		Label(FrameKet,text="Rental OKE adalah sebuah aplikasi yang mencatat pelanggan yang meminjam kendaraan\n",font=("bold"),anchor="w",foreground="black").grid(column = 0)	
		Label(FrameKet,text="Pembuat : Dikdik Darmawan (1901002)\n",font=("bold"),anchor="w",foreground="black").grid(column = 0)
		Button(FrameKet,text="Close",command=FrameKet.destroy).grid(column = 0)
		pass

	def CloseProgram(self):
		response = messagebox.askquestion("Peringatan", "Apakah Anda Serius Ingin Keluar ?")
		if(response == "yes"):
			self.root.destroy()
		pass
