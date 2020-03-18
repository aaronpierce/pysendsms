# test_contact.py

import pysendsms
from tests.tools import raise_error

def test_invalid_number():

    error_message = 'Bad number input: Ex."277-453-2453"'

    assert raise_error(ValueError, pysendsms.Contact, '702851171', 'AT&T', msg=error_message)          # Short
    assert raise_error(ValueError, pysendsms.Contact, '7028511711000', 'AT&T', msg=error_message)      # Long
    assert raise_error(ValueError, pysendsms.Contact, '702^851^1711', 'AT&T', msg=error_message)       # Bad Special Char
    assert raise_error(ValueError, pysendsms.Contact, '7O2851171', 'AT&T', msg=error_message)          # Alphanumeric
    assert raise_error(ValueError, pysendsms.Contact, '+11-702-8511-711','AT&T', msg=error_message)    # Bad Number Grouping

def test_valid_number():

    assert pysendsms.Contact('7028511711','AT&T')
    assert pysendsms.Contact('702-8511711','AT&T')
    assert pysendsms.Contact('702851-1711','AT&T')
    assert pysendsms.Contact('702-851-1711','AT&T')
    assert pysendsms.Contact('17028511711','AT&T')
    assert pysendsms.Contact('1-7028511711','AT&T')
    assert pysendsms.Contact('+1-702-851-1711','AT&T')
    assert pysendsms.Contact('+11-702-851-1711','AT&T')

def test_valid_carrier():

    assert pysendsms.Contact('2775551212', 'AT&T')
    assert pysendsms.Contact('2775551212', 'Bluegrass Cellular')
    assert pysendsms.Contact('2775551212', 'ProPage')
    assert pysendsms.Contact('2775551212', 'US Cellular')

def test_invalid_carrier():

    error_message = 'Bad carrier input. Check pysendsms.CARRIERS for options.'

    assert raise_error(KeyError, pysendsms.Contact, '2775551212', 'ATT', msg=error_message)        # Not in CARRIERS
    assert raise_error(KeyError, pysendsms.Contact, '2775551212', 123, msg=error_message)          # Not in CARRIERS
    assert raise_error(KeyError, pysendsms.Contact, '2775551212', ' ', msg=error_message)          # Not in CARRIERS
    assert raise_error(KeyError, pysendsms.Contact, '2775551212', 'USCellular', msg= error_message) # Not in CARRIERS

def test_valid_fulladdress():

    assert pysendsms.Contact.by_address('example@gmail.com')
    assert pysendsms.Contact.by_address('example@sample.mail.com')

def test_invalid_fulladdress():

    error_message = 'Bad address given. Expected <example>@<domain>.<toplevel-domain>'

    assert raise_error(ValueError, pysendsms.Contact.by_address, 'examplegmail.com', msg=error_message)
    assert raise_error(ValueError, pysendsms.Contact.by_address, '', msg=error_message)

def test_valid_contact_init():

    assert pysendsms.Contact(number='+12775552222', carrier='AT&T')
    assert pysendsms.Contact.by_address('example@gmail.com')

def test_invalid_contact_init():

    error_message = 'Must provide number & carrier or full address.'
    
    assert raise_error(ValueError, pysendsms.Contact, carrier='AT&T', msg=error_message)
    assert raise_error(ValueError, pysendsms.Contact, msg=error_message)

    error_message = 'Must provide carrier information with number.'

    assert raise_error(ValueError, pysendsms.Contact, number='+12775552222', msg=error_message)