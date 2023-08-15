class Mangga:

	#magic method
    # akan otomatis dijalankan saat pertama kali objek dibuat
	def __init__(self,nama,jumlah):
		self.nama = nama
		self.jumlah = jumlah

    # repr biasanya dipakai untuk debug (untuk programmer)
	def __repr__(self):
		return "Debug - Mangga: {} dengan jumlah: {}".format(self.nama,self.jumlah)

    # str biasanya dipakai saat produksi (untuk user)
	def __str__(self):
		return "Mangga: {} dengan jumlah: {}".format(self.nama,self.jumlah)

    # add biasa dipakai untuk operasi matematika, ada juga yang lain seperti sub, mul, div, dll
	def __add__(self,objek):
		return self.jumlah + objek.jumlah

    # kita dapat mengubah behavior dari suatu magic method 
	@property
	def __dict__(self):
		return "objek ini mempunyai nama dan jumlah"

    # magic method lainnya dapat dilihat di documentation python

belanja1 = Mangga("arumanis",10)
belanja2 = Mangga("mana lagi",30)
print(repr(belanja1))
print(belanja2)
print(belanja1 + belanja2)
print(belanja1.__dict__)