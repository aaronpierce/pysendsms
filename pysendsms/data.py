# data.py

import pkgutil

def load_file():
    """ A function to load carriers.json file from disk and return raw string data.
  
    Returns: 
        pkguti.get_data().decode() : str
            String representation of the carriers.json file loaded from disk.
    """

    return pkgutil.get_data(__name__, "./carriers.json").decode()
