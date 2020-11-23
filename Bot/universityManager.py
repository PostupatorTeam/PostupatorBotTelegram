from dataclasses import dataclass

@dataclass
class University:
    paymentForm: str
    studyForm: str
    directionStudy: str
    studyProgram: str
    universityBranch: str
    name: str


def add_university_info(info,user):
    if user.universities[-1].name == 'ЛЭТИ':
        if user.universities[-1].studyProgram == None:
            user.universities[-1].studyProgram = info
            return 'Введите форму обучения'
        if user.universities[-1].paymentForm == None:
            user.universities[-1].studyProgram = info
            return None
    if user.universities[-1].name == 'РАНХГИС':
        if user.universities[-1].universityBranch == None:
            user.universities[-1].universityBranch = info
            return 'Введите направление обучения'
        if user.universities[-1].directionStudy == None:
            user.universities[-1].directionStudy = info
            return 'Введите форму обучения'
        if user.universities[-1].studyForm == None:
            user.universities[-1].studyForm = info
            return 'Введите программу обучения'
        if user.universities[-1].studyProgram == None:
            user.universities[-1].studyProgram = info
            return None
    if user.universities[-1].name == 'СГУ':
        if user.universities[-1].directionStudy == None:
            user.universities[-1].directionStudy = info
            return 'Введите форму обучения'
        if user.universities[-1].studyForm == None:
            user.universities[-1].studyForm = info
            return 'Введите форму оплаты'
        if user.universities[-1].paymentForm == None:
            user.universities[-1].studyProgram = info
            return None

def get_first_message(university):
    if university == 'ЛЭТИ':
        return 'Введите программу обучения'
    if university == 'РАНХГИС':
        return 'Введите филиал вуза'
    if university == 'СГУ':
        return 'Введите направление обучения'
