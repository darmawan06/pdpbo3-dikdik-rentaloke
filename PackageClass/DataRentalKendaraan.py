class DataRentalKendaraan:
	"""docstring for DataRentalKendaraan"""
	def __init__(self,NoKTP,Nama,NamaKendaraan,JenisKendaraan,Aksesoris,Warna,locationPhoto):
		super(DataRentalKendaraan, self).__init__()
		self.NoKTP = NoKTP
		self.Nama = Nama
		self.NamaKendaraan = NamaKendaraan
		self.JenisKendaraan = JenisKendaraan
		self.Aksesoris = ""
		for x in Aksesoris:
			self.Aksesoris += x + '\n'
			pass
		self.Warna = Warna
		self.Photo = 'null'
		if(locationPhoto != ""):
			self.Photo = locationPhoto
	pass

