# diamond problem

class A:
	
	def show(self):
		print("ini adalah show A")

class B(A):
	
	def show(self):
		print("ini adalah show B")

class C(A):
	
	def show(self):
		print("ini adalah show C")

class D(B,C):
	pass

objek = D()
objek.show()
print(D.__mro__) # method resolution order
# urutan pengecekan method
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

help(objek)