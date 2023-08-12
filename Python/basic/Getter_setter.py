class Hero:

	def __init__(self, name, health, armor):
		self.name = name
		self.__health = health
		self.__armor = armor
		# self.info = "name {} : \n\thealth: {}".format(self.name,self.__health) <-- tidak efektif, karena jika ada perubahan pada method, maka tidak akan berubah

	@property # merubah method menjadi seperti variabel
	# property bersifat dinamis, jadi jika ada perubahan pada method, maka akan berubah juga
	def info(self):
		return "name {} : \n\thealth: {}".format(self.name,self.__health)

    # contoh property untuk modifikasi variabel private
	@property 
	def armor(self):
		pass

	@armor.getter 
	def armor(self):
		return self.__armor

    # menggunakan setter untuk mengubah variabel private akan lebih simple
	@armor.setter
	def armor(self, input):
		self.__armor = input

    # jika ingin menghapus variabel private, maka harus menggunakan deleter
	@armor.deleter
	def armor(self):
		print('armor di delet')
		self.__armor = None

sniper = Hero('sniper',100,10)

print('merubah info')
print(sniper.info)
sniper.name = 'dadang'
print(sniper.info)

print('getter dan setter untuk __armor:')
print(sniper.armor)
sniper.armor = 50
print(sniper.armor)

print('delete armor')
del sniper.armor
print(sniper.__dict__)