# pysendsms
Quick and simple way to send SMS via Gmail to known a cell carrier.

sms = pysendsms.SMS('<username>@gmail.com', '<password>')

contact = pysendsms.Contact('1-276-854-3723', pysendsms.CARRIERS['Bluegrass Cellular']["0"])

sms.send(contact, 'Hello, World!')