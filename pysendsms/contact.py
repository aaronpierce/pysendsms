# contact.py

from json import loads
import re
from . import data

CARRIERS = loads(data.load_file())


class Contact:
    def __init__(self, number, carrier):

        self.number = Contact.validate_phone(number)
        self.carrier = Contact.validate_carrier(carrier)


    def __repr__(self):
        return f'{self.number}{self.carrier}'

    def address(self):
        return repr(self)

    @staticmethod
    def validate_phone(number):
        matcher = re.compile(r'^\+?\d{0,2}-?\d{3}-?\d{3}-?\d{4}$')
        if re.match(matcher, number):
            return number.replace('-', '').replace('+', '')
        else:
            raise ValueError('Bad phone number')

    @staticmethod
    def validate_carrier(carrier):
        if (c := CARRIERS.get(carrier)):
            return c
        else:
            raise KeyError('Bad Carrier input. Check pysendsms.CARRIERS for options.')