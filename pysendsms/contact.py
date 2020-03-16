# contact.py

from json import loads
import re
from . import data

CARRIERS = loads(data.load_file())


class Contact:
    """ A class for storing information of a point of communication for relaying messages to.
      
    Attributes: 
        number : str 
            Phone number to send information to.
        carrier : str
             Name of which carrier provides the receiving service.
    """
  
    def __init__(self, number, carrier):
        """ The constructor for Contact class. """

        self.number = Contact.validate_phone(number)
        self.carrier = Contact.validate_carrier(carrier)


    def __repr__(self):
        """ The __repr__ function to retrieve identifyable information about the instanced Contact.

        Returns: 
            str(self.nubmer, self.carrier) : str
                A concatination of both attribute strings.
        """

        return f'{self.number}{self.carrier}'

    def address(self):
        """ A function to call to retrieve the email address associated with this Contact isntance.

        Returns: 
            __repr__(): str
                A concatination of both attribute strings. str(self.nubmer, self.carrier) <phonenumber>@<email>
        """
        
        return repr(self)

    @staticmethod
    def validate_phone(number):
        """ A function to validate number is a string of digits of 10-12 in length. 
  
        Parameters: 
            number : str
                A string of digits corresponding to a phone number.
          
        Returns: 
            number : str
                The incoing string with '-' replaced by '' to appease formatting.
        """

        matcher = re.compile(r'^\+?\d{0,2}-?\d{3}-?\d{3}-?\d{4}$')
        if re.match(matcher, number):
            return number.replace('-', '').replace('+', '')
        else:
            raise ValueError('Bad phone number')

    @staticmethod
    def validate_carrier(carrier):
        """ A function to validate carrier is found in CARRIER dictionary.
  
        Parameters: 
            carrier : str
                A string of digits corresponding to a phone number.
          
        Returns: 
            c : str
                Key of the CARRIER dictionary accessed from carrier parameter.
        """

        if (c := CARRIERS.get(carrier)):
            return c
        else:
            raise KeyError('Bad Carrier input. Check pysendsms.CARRIERS for options.')
