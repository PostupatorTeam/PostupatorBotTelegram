from dataclasses import dataclass


@dataclass
class Program:
    paymentForm: str
    studyForm: str
    directionStudy: str
    studyProgram: str
    universityBranch: str
    universityName: str


def add_program_info(info, student):
    if student.programs[-1].universityName == 'ЛЭТИ':
        if student.programs[-1].studyProgram is None:
            student.programs[-1].studyProgram = info
            return 'Введите форму обучения'
        if student.programs[-1].paymentForm is None:
            student.programs[-1].paymentForm = info
            return None
    if student.programs[-1].universityName == 'РАНХГИС':
        if student.programs[-1].universityBranch is None:
            student.programs[-1].universityBranch = info
            return 'Введите направление обучения'
        if student.programs[-1].directionStudy is None:
            student.programs[-1].directionStudy = info
            return 'Введите форму обучения'
        if student.programs[-1].studyForm is None:
            student.programs[-1].studyForm = info
            return 'Введите программу обучения'
        if student.programs[-1].studyProgram is None:
            student.programs[-1].studyProgram = info
            return None
    if student.programs[-1].universityName == 'СПБГУ':
        if student.programs[-1].directionStudy is None:
            student.programs[-1].directionStudy = info
            return 'Введите форму обучения'
        if student.programs[-1].studyForm is None:
            student.programs[-1].studyForm = info
            return 'Введите форму оплаты'
        if student.programs[-1].paymentForm is None:
            student.programs[-1].paymentForm = info
            return None


def get_first_message(university):
    if university == 'ЛЭТИ':
        return 'Введите программу обучения'
    if university == 'РАНХГИС':
        return 'Введите филиал вуза'
    if university == 'СПБГУ':
        return 'Введите направление обучения'
