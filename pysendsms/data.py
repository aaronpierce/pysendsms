import pkgutil

def load_file():
    return pkgutil.get_data(__name__, "./carriers.json").decode()
