# contact.py

from json import loads
import re
from . import data

CARRIERS = loads(data.load_file())


class Contact:
    """ A class for storing information of a point of communication for relaying messages to.

    Attributes:
    -------------------
       filladdress : str
            Email formatted string for sending messages to.
       number : str
            Phone number to send information to.
        carrier : str
             Name of which carrier provides the receiving service.
    """

    def __init__(self, number=None, carrier=None, fulladdress=None):
        """ The initilizer for Contact class. """

        self.fulladdress = fulladdress
        self.number = number
        self.carrier = carrier


    @classmethod
    def by_address(cls, fulladdress):
        """ Class method used as an alternate way to built a Contact by taking the whole address directly as string.

        Attributes:
        ----------------
            fulladdress : str
                Email formatted string for sending messages to.
        """
        if '@' in fulladdress:
            return cls(fulladdress=fulladdress)
        else:
            raise ValueError('Bad address given. Expected <example>@<domain>.<toplevel-domain>')

    def __repr__(self):
        """ The __repr__ function to retrieve identifiable information about the instanced Contact.

        Returns:
        -------------------
            f"<Contact('<intilizer-values>')>" : str
                A class identifier with stored attributes shown.
        """
        if self.fulladdress is None:
            return f"<Contact('{self.number}', '{self.carrier}')>"
        else:
            return f"<Contact('{self.fulladdress}')>"

    @property
    def address(self):
        """ An attribute used retrieve the email address associated with this Contact instance.

        Returns:
        -------------------
           address : str
                A strings representationg of an sms address.(Ex. <phonenumber>@<email>)
        """
        address = f'{self.number}{self.carrier}' if self.fulladdress is None else self.fulladdress
        return address

    @property
    def number(self):
        """ Attribute that contains phone number for email address """
        return self._number

    @number.setter
    def number(self, value):
        """ Property setter to validate number is a string of digits of 10-12 in length and formatted properly.

        Parameters:
        -------------------
            value : str
                A string of digits corresponding to a phone number.
        """

        if self.fulladdress:
            self._number = None
            return
        elif not value:
            raise ValueError('Must provide number & carrier or full address.')

        if type(value) != str:
            raise TypeError('You must pass the number argument as a string.')

        matcher = re.compile(r'^\+?\d{0,2}-?\d{3}-?\d{3}-?\d{4}$')
        if re.match(matcher, value):
            self._number = value.replace('-', '').replace('+', '')
        else:
            raise ValueError('Bad number input: Ex."277-453-2453"')

    @property
    def carrier(self):
        """ Attribute that contains domain portion of email address """
        return self._carrier

    @carrier.setter
    def carrier(self, value):
        """ Property setter to validate carrier is found in CARRIER dictionary.

        Parameters:
        -------------------
            value : str
                A string of for carrier name corresponding to keys in CARRIER dict.
        """

        if self.fulladdress:
            self._carrier = None
            return
        elif not value:
            raise ValueError('Must provide carrier information with number.')

        if CARRIERS.get(value, False):
            self._carrier = CARRIERS[value]
        else:
            raise KeyError('Bad carrier input. Check pysendsms.CARRIERS for options.')
