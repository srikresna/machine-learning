class Hero:

	#private class variabel
	__jumlah = 0;

	def __init__(self,name):
		# variabel instance private
		self.__name = name
		Hero.__jumlah += 1

	# method ini hanya berlaku untuk objek
	def getJumlah(self):
		return Hero.__jumlah

	# method ini tidak berlaku untuk objek tapi berlaku untuk class
	def getJumlah1():
		return Hero.__jumlah

	# method static (decorator) nempel ke objek dan class
	@staticmethod
	def getJumlah2():
		return Hero.__jumlah

    # method class (decorator) nempel ke class
	@classmethod
	def getJumlah3(cls):
		return cls.__jumlah
	
'''
perbedaan class method dan tanpa decorator
    1. class method mempunyai parameter cls (class)
    2. class method hanya bisa mengakses class variabel
    3. class method tidak bisa mengakses instance variabel
    4. class method bisa diakses oleh objek dan class
    5. parameter cls bisa diganti dengan nama lain, tapi tetap merepresentasikan class
'''

sniper = Hero('sniper')
print(Hero.getJumlah2())
rikimaru = Hero('rikimaru')
print(sniper.getJumlah2())
drowranger = Hero('drowranger')