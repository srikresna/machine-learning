# method resolution order // multiple inheritance
# ketika penamaan sama

class A:
	
	def show(self):
		print("ini adalah show A")

class B:

	def show(self):
		print("ini adalah show B")

class C(B,A):
	pass
	


objek = C()
objek.show()
help(objek)