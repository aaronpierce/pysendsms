# sms.py

import smtplib
import contact

class SMS():
	def __init__(self, email, password):
		self.server = smtplib.SMTP('smtp.gmail.com', 587)
		self.email = email
		self.password = password

	def connect(self, contact, message):
		with self.server as gmail:
			gmail.starttls()
			gmail.login(self.email, self.password)

			gmail.sendmail(self.email, contact.address(), message)

	def send(self, contact, message):
		self.connect(contact, message)



if __name__ == '__main__':
	creds = ('aaronpierce15@gmail.com', 'qqipjittpdznntqz')

	sms = SMS(*creds)

	aaron = contact.Contact('2705852271', contact.CARRIERS['Bluegrass Cellular']["0"])

	#sms.send(aaron, 'Hello!')

