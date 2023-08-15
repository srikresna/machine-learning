from abc import ABC,abstractmethod

class Button(ABC):

	def __init__(self,set_link):
		self.link = set_link

	@abstractmethod
	def click(self):
		pass

	@property # dari attribut link diubah menjadi method link
	@abstractmethod
	def link(self):
		pass


class PushButton(Button):
	
	def click(self):
		print("Go To: {}".format(self.link))

	@Button.link.setter
	def link(self,input):
		self.__link = input

	@link.getter # tidak define Button karena sudah di define di atas
	def link(self):
		return self.__link	



tombol1 = PushButton("www.kelasterbuka.id")
tombol1.click()	