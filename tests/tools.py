# tools.py

import pytest
from functools import wraps

def match_error(func):
    @wraps(func)
    def wrapper(*args, msg, **kwargs):
        e = func(*args, **kwargs)
        error = str(e.value)
        message = "'"+msg+"'" if error[0] == "'" else msg
        return error == message
    return wrapper

@match_error
def raise_error(err, test, *args, **kwargs):
    with pytest.raises(err) as e:
        test(*args, **kwargs)
    return e
