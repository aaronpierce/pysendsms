# tools.py

import pytest
from functools import wraps

def match_error(func):
    """ Wrapper that takes result of a function that returns an error and matches it to a given message."""

    @wraps(func)
    def wrapper(*args, msg, **kwargs):
        e = func(*args, **kwargs)
        error = str(e.value)
        message = "'"+msg+"'" if error[0] == "'" else msg
        return error == message
    return wrapper

@match_error
def raise_error(err, test, *args, **kwargs):
    """ Function to run an expression inside a pytest with statement to capture an exception and return it.

    Parameters
    --------------
        err : Exception
            The subclass type of an Exception that you would like to predict. (Ex. TypeError)
        test : Object()
            Any object that is callable that you intend to catch the errors of.
        msg : str
            msg should be passed to compare againse the error message. Captured by **kwargs and used within wrapper.
    """

    with pytest.raises(err) as e:
        test(*args, **kwargs)
    return e
