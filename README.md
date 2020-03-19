<img width="200" alt="portfolio_view" src="https://github.com/aaronpierce/pysendsms/blob/master/resources/PySendSMS.png">  

# PySendSMS

pysendsms is a quick and simple way to use python to send SMS via Gmail or any other SMTP servers to known a cell carrier.

## Installation

Use the package manager [pip](https://pypi.org/project/pysendsms) to install pysendsms.

```bash
pip install pysendsms
```

## Requires

 - A Gmail account with app specific password enabled for use. [Manage Google Apps](https://myaccount.google.com/apppasswords)

>  Note: Other SMTP servers can be used, however configuration varies by providers. Gmail is setup to work by default just requiring email and password.

- Knowledge of which cell carrier provider the receiving party uses.

## Usage

Import the library and create an SMS Object utilizing your gmail account and an application password created within your Google account.

```python
import pysendsms

sms = pysendsms.SMS('<username>@gmail.com', '<app-password>')
```
SMS object has various parameters allowing you to use some other SMTP providers of your choice.
```python
sms = pysendsms.SMS(self,
					username='<username>@gmail.com',
					password= '<app-password>',
					from_email=None,
					server='smtp.gmail.com',
					port=587,
					tls=True)
```
>Note: If using an SMTP API and you are given a username that is not an email address, you must provide the a verified from_email parameter otherwise outgoing mail with fail.

Create an Contact object using the persons phone number and select a carrier from the available options.
  
CARRIERS is a dictionary loaded from a json file in the project that can be checked for available carriers that can be used for messaging.
  
```python
>>> pysendsms.Contact('2715552343', 'AT&T')
<Contact('2715552343', '@mms.att.net')>
```
A Contact can also be created with a known address using the by_address class method.
```python
>>> pysendsms.Contact.by_address('2715552343@mms.att.com')
<Contact('2715552343@mms.att.com')>
```
>Note: Given the nature of this capability, you are able to just add any email address here and not one linked to a phone number for standard SMTP emailing functionality.


Use the SMS.send() method of your SMS object, passing the Contact and the message you would like to send as a string. This can also accept a list of contacts for sending out group messages.
```python
contact1 = pysendsms.Contact('311-555-2368', 'AT&T')

sms.send(contact1, 'Hello, World!')

contact2 = pysendsms.Contact.by_address('3115552368@mms.att.net')

group = [contact1, contact2]

sms.send(group, 'Everyone gets a message!')
```

## License
  
[MIT](https://choosealicense.com/licenses/mit/)