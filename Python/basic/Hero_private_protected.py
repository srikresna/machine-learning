class Hero:
	# class variabel
	jumlah = 0
	# private class variabel
	__privateJumlah = 0

	def __init__(self,name,health,attackPower,armorNumber):
		# variabel instance private
		self.name = name
		self.health = health
		self.attackPower = attackPower
		self.armorNumber = armorNumber
		Hero.jumlah += 1
		# variabel instance protected
		self.__private = "private"
		# variabel instance protected
		self._protected = "protected"


	# void function, method tanpa return
	def siapa(self):
		print("namaku adalah " + self.name)

	# method dengan argumen
	def healthUp(self,up):
		self.health += up

	# method dengan return
	def getHealth(self):
		return self.health

	def serang(self, lawan):
		print(self.name + ' menyerang ' + lawan.name )
		lawan.diserang(self, self.attackPower)
	
	def diserang(self, lawan, attackPower_lawan):
		print(self.name + ' diserang ' + lawan.name)
		attack_diterima = attackPower_lawan/self.armorNumber
		print('serangan terasa : ' + str(attack_diterima))
		self.health -= attack_diterima
		print('darah ' + self.name + ' tersisa ' + str(self.health))

sniper = Hero('sniper',100,10,5)
rikimaru = Hero('rikimaru',100,20,10)

print(sniper.__dict__)
print(rikimaru.__dict__)
print(Hero.__dict__)
# print(Hero.__privateJumlah) # error karena private

# sniper.serang(rikimaru)
# print("\n")
# rikimaru.serang(sniper)
# print("\n")
# rikimaru.serang(sniper)
# print("\n")
# rikimaru.serang(sniper)
# print("\n")
# rikimaru.serang(sniper)
# print("\n")
# rikimaru.serang(sniper)