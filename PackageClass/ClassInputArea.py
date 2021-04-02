from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image

class InputArea(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		self.parent = parent;
		self.InputNoKTP = Entry(self.parent,width=25)
		self.InputNoKTP.insert(0,"")
		self.InputNama = Entry(self.parent,width=25)
		self.InputNama.insert(0,"")
		self.InputNamaKendaraan = Entry(self.parent,width=25)
		self.InputNamaKendaraan.insert(0,"")
		self.ValueJenisKendaraan = StringVar(self.parent)
		self.ValueAksesoris1 = StringVar(self.parent)
		self.ValueAksesoris2 = StringVar(self.parent)
		self.ValueAksesoris3 = StringVar(self.parent)
		self.ValueAksesoris4 = StringVar(self.parent)
		self.ValueWarna = StringVar(self.parent)
		pass

	def Draw(self,frame):
		# Membuat Label
		Label(frame,text="No KTP :").grid(column=0,row=0)
		Label(frame,
			text="Nama :"
			).grid(column=0,row=1)
		Label(frame,text="Nama Kendaraan :").grid(column=0,row=2)
		Label(frame,text="Jenis Kendaraan :").grid(column=0,row=3)
		Label(frame,text="Aksesoris Kendaraan :").grid(column=0,row=4)
		Label(frame,text="Warna Mobil :").grid(column=0,row=8)

		# Membuat Proses Input
		self.InputNoKTP = Entry(self.parent,width=25)
		self.InputNoKTP.insert(0,"")
		self.InputNama = Entry(self.parent,width=25)
		self.InputNama.insert(0,"")
		self.InputNamaKendaraan = Entry(self.parent,width=25)
		self.InputNamaKendaraan.insert(0,"")
		self.InputNoKTP.grid(column=1,row=0)
		self.InputNama.grid(column=1,row=1)
		self.InputNamaKendaraan.grid(column=1,row=2)
		ListJenisKendaraan = ["Normal","Sport","Racing","OffRoad"]		
		self.ValueJenisKendaraan.set(ListJenisKendaraan[0])
		DropdownJenisKendaraan = OptionMenu(frame,
			self.ValueJenisKendaraan,
			*ListJenisKendaraan)
		DropdownJenisKendaraan.config(width=20)
		DropdownJenisKendaraan.grid(column=1,row=3)
		listValueAksesoris = ["Lampu Cadangan","Ban Candangan","GPS","Pengharum"]
		cb1 = Checkbutton(frame,text=listValueAksesoris[0],variable = self.ValueAksesoris1,justify=LEFT,onvalue = listValueAksesoris[0], offvalue="Null")
		cb2 = Checkbutton(frame,text=listValueAksesoris[1],variable = self.ValueAksesoris2,justify=LEFT,onvalue = listValueAksesoris[1], offvalue="Null")
		cb3 = Checkbutton(frame,text=listValueAksesoris[2],variable = self.ValueAksesoris3,justify=LEFT,onvalue = listValueAksesoris[2], offvalue="Null")
		cb4 = Checkbutton(frame,text=listValueAksesoris[3],variable = self.ValueAksesoris4,justify=LEFT,onvalue = listValueAksesoris[3], offvalue="Null")
		cb1.deselect()
		cb2.deselect()
		cb3.deselect()
		cb4.deselect()
		cb1.grid(column=1,row=4)
		cb2.grid(column=1,row=5)
		cb3.grid(column=1,row=6)
		cb4.grid(column=1,row=7)
		ListWarna = ["Merah","Kuning","Hitam","Abu-Abu"]
		baris = 8
		self.ValueWarna = StringVar(self.parent)
		for var in ListWarna:
			Radiobutton(frame,
					text=var,
					variable=self.ValueWarna,
					value=var).grid(column=1,row=baris)
			baris = baris + 1
		pass

	def GetValueNoKTP(self):
		return self.InputNoKTP.get()
		pass

	def GetValueNama(self):
		return self.InputNama.get()
		pass

	def GetValueNamaKendaraan(self):
		return self.InputNamaKendaraan.get()
		pass

	def GetValueJenisKendaraan(self):
		return self.ValueJenisKendaraan.get()
		pass

	def GetValueAksesoris(self):
		ValueAksesoris = []
		if(self.ValueAksesoris1.get() != "Null"):
			ValueAksesoris.append(self.ValueAksesoris1.get())
		
		if(self.ValueAksesoris2.get() != "Null"):
			ValueAksesoris.append(self.ValueAksesoris2.get())
		
		if(self.ValueAksesoris3.get() != "Null"):
			ValueAksesoris.append(self.ValueAksesoris3.get())
		
		if(self.ValueAksesoris4.get() != "Null"):
			ValueAksesoris.append(self.ValueAksesoris4.get())
		return ValueAksesoris
		pass

	def GetValueWarna(self):
		return self.ValueWarna.get()
		pass

	pass