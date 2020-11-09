users = {}

class User:
    def __init__(self):
        self.firstName = None
        self.surname = None
        self.patronymic = None
        self.points = None

def add_data(id,answer):
    if users[id].firstName == None:
        add_firstName_user(id,answer)
        return 0
    if users[id].surname == None:
        add_surname_user(id,answer)
        return 1
    if users[id].patronymic == None:
        add_patronymic_user(id,answer)
        return 2
    if users[id].points == None:
        add_points_user(id,answer)
        return 3
    return 4

def add_user(id):
    users[id] = User()

def add_firstName_user(id,name):
    users[id].firstName = name

def add_surname_user(id,name):
    users[id].surname = name

def add_patronymic_user(id,name):
    users[id].patronymic = name

def add_points_user(id,points):
    users[id].points = points

def get_firstName_user(id):
    return users[id].firstName

def get_last_Name_user(id):
    return users[id].lastName

def get_patronymic_user(id):
    return users[id].patronymic

def get_points_user(id):
    return users[id].points


