# sms.py

import smtplib

class SMS():
	def __init__(self, email, password):
		self.server = smtplib.SMTP('smtp.gmail.com', 587)
		self.email = email
		self.password = password

	def connect(self, contacts, message):
		with self.server as gmail:
			gmail.starttls()
			gmail.login(self.email, self.password)

			if type(contacts) != type(list()):
				contacts = [contacts]

			for contact in contacts:
				gmail.sendmail(self.email, contact.address(), message)

	def send(self, contacts, message):
		self.connect(contacts, message)