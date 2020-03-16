# pysendsms
pysendsms is a quick and simple way to use python to send SMS via Gmail SMTP servers to known a cell carrier.

  

## Installation

  

Use the package manager [pip](https://pypi.org/project/pysendsms) to install pysendsms.

  

```bash
pip install pysendsms
```
## Requires
  - A Gmail account with app specific password enabled for use. [Manage Google Apps](https://myaccount.google.com/apppasswords)
  - Knowledge of which cell carrier provider the receiving party uses.
  

## Usage

  

Import the library and create an SMS Object utilizing your gmail account and an application password created within your Google account.

  

```python
import pysendsms

sms = pysendsms.SMS('<username>@gmail.com', '<app-password>')
```

Create an Contact object using the persons phone number and select a carrier from the available options.

CARRIERS is a dictionary loaded from a json file in the project that can be checked for available carriers that can be used for messaging.

```python
contact = pysendsms.Contact('311-555-2368', 'AT&T')
```

  

Use the SMS.send() method of your SMS object, passing the Contact and the message you would like to send as a string.

```python
sms.send(contact, 'Hello, World!')
```

SMS.send() can also accept a list of contacts for sending out group messages.

```python
group = [contact, contact, contact, contact]

sms.send(group, 'Everyone gets a message!')
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
