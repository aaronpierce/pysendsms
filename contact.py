# contact.py

from json import load

CARRIERS = load(open('carriers.json'))

class Contact:
	def __init__(self, number, carrier):
		self.number = number
		self.carrier = carrier

	def __repr__(self):
		return f'{self.number}{self.carrier}'

	def address(self):
		return repr(self)
