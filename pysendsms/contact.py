# contact.py

from json import loads
import re
from . import data

CARRIERS = loads(data.load_file())


class Contact:
    def __init__(self, number, carrier):
        if not self.validate(number):
            raise ValueError("Bad phone number")

        self.carrier = carrier

    def __repr__(self):
        return f'{self.number}{self.carrier}'

    def address(self):
        return repr(self)

    def validate(self, number):
        matcher = re.compile(r'^\+?\d{0,2}-?\d{3}-?\d{3}-?\d{4}$')
        if re.match(matcher, number):
            self.number = number.replace('-', '').replace('+', '')
            state = True
        else:
            state = False

        return state
