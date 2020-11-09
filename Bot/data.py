users = {}

class User:
    def __init__(self):
        self.firstName = None
        self.lastName = None
        self.points = None

def add_user(id):
    users[id] = User()

def add_firstName_user(id,name):
    users[id].firstName = name

def add_lastName_user(id,name):
    users[id].lastName = name

def add_points_user(id,points):
    users[id].points = points

def get_firstName_user(id):
    return users[id].firstName

def get_last_Name_user(id):
    return users[id].lastName

def get_points_user(id):
    return users[id].points


