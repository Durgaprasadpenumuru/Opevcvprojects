class computer:
	def __init__(self,typ,make,warranty):
		self.typ = typ
		self.make = make
		self.warranty=warranty
	def info(self):
		print("computer is"+self.typ+"and make is "+self.make)
	def set_warranty(self,a):
		self.warranty=a
	def get_warranty(self):
		return self.warranty
c=computer("crt","dell","warranty")
c.make="lenova"
c1=computer("lap","acer",13)
c1.info()
c1.set_warranty(12)
c1.info()
c.info()