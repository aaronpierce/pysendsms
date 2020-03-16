import pytest
import pysendsms


def test_validate_phone_invalid():
    bad_numbers = [
        '702851171',        #Short
        '7028511711000',    #Long
        '702^851^1711',     #Bad Special Char
        '7O2851171',        #Alphanumeric
        '+11-702-8511-711'  #Misplaced Special Char
        ]

    for number in bad_numbers:
        with pytest.raises(ValueError):
            pysendsms.Contact.validate_phone(number)

def test_validate_phone_valid():
    good_numbers = [
        '7028511711',
        '702-8511711',
        '702851-1711',
        '702-851-1711',
        '17028511711',
        '1-7028511711',
        '+1-702-851-1711',
        '+11-702-851-1711'
    ]
    
    for number in good_numbers:
        assert pysendsms.Contact.validate_phone(number)