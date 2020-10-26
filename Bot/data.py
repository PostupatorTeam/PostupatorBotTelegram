

class User:

    def __init__(self):
        self.firstName = None
        self.lastName = None

def add_firstName(id,name,users):
    if not id in users:
        users[id] = User()
    users[id].firstName = name

def add_lastName(id,name,users):
    if not id in users:
        users[id] = User()
    users[id].lastName = name

