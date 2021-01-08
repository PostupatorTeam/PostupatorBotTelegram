from typing import Optional
from src.main.middle_module import middle_module
from src.main.telegram_module.converters.converters import convert_to_student_database, convert_to_message
from src.main.telegram_module.models import models_storage
from src.main.telegram_module.models.models_storage import RegistrationData, Student
from src.main.telegram_module.validators.validator import is_validate_university


students = {}
is_create = None


def add_first_name_to_user(student: Student, name: str):
    student.name = name


def add_surname_user(student: Student, name: str):
    student.surname = name


def add_lastname_to_user(student: Student, name: str):
    student.lastname = name


def add_program_to_user(student: Student, university: str):
    student.programs.append(models_storage.Program(None, None, None, None, None, university))


def add_program_info(info: str, student: Student) -> Optional[str]:
    if student.programs[-1].university_name == 'ЛЭТИ':
        if student.programs[-1].program is None:
            student.programs[-1].program = info
            return 'Введите форму обучения'

        if student.programs[-1].pay_form is None:
            student.programs[-1].pay_form = info
            return None

    if student.programs[-1].university_name == 'РАНХИГС':
        if student.programs[-1].university_branch is None:
            student.programs[-1].university_branch = info
            return 'Введите направление обучения'

        if student.programs[-1].approval is None:
            student.programs[-1].approval = info
            return 'Введите форму обучения'

        if student.programs[-1].educational_form is None:
            student.programs[-1].educational_form = info
            return 'Введите программу обучения'

        if student.programs[-1].program is None:
            student.programs[-1].program = info
            return None

    if student.programs[-1].university_name == 'СПБГУ':
        if student.programs[-1].approval is None:
            student.programs[-1].approval = info
            return 'Введите форму обучения'

        if student.programs[-1].educational_form is None:
            student.programs[-1].educational_form = info
            return 'Введите форму оплаты'

        if student.programs[-1].pay_form is None:
            student.programs[-1].pay_form = info
            return None


def get_first_message(university: str) -> str:
    if university == 'ЛЭТИ':
        return 'Введите программу обучения'
    if university == 'РАНХИГС':
        return 'Введите филиал вуза'
    if university == 'СПБГУ':
        return 'Введите программу обучения'


def add_user(chat_id: int):
    students[chat_id] = models_storage.Student(None, None, None, [], False, True)


def end_registration(chat_id: int) -> str:
    students[chat_id].is_registered = True
    student = convert_to_student_database(students[chat_id], str(chat_id))
    del students[chat_id]

    universities_data = middle_module.edit_user(student) if not is_create else \
        middle_module.create_user(student)

    return convert_to_message(universities_data)


# Строки для взаимодействия с пользователем
def add_data_to_user(chat_id: int, message: str, data_type: RegistrationData) -> Optional[str]:
    if data_type == RegistrationData.Empty:
        add_user(chat_id)
        return 'Введите имя'

    if data_type == RegistrationData.Name:
        add_first_name_to_user(students[chat_id], message)
        return 'Введите фамилию'

    if data_type == RegistrationData.Surname:
        add_surname_user(students[chat_id], message)
        return 'Введите отчество'

    if data_type == RegistrationData.Patronymic:
        add_lastname_to_user(students[chat_id], message)
        return 'Укажите университет'

    if data_type == RegistrationData.University_Name:
        if is_validate_university(students[chat_id], message):
            add_program_to_user(students[chat_id], message)
            students[chat_id].is_added_program = False
            return get_first_message(message)
        else:
            return 'Введите университет из списка или закончите регистрацию'

    if data_type == RegistrationData.Program_Info:
        response = add_program_info(message, students[chat_id])
        if response is None:
            students[chat_id].is_added_program = True
            return 'Укажите университет'
        else:
            return response

    if data_type == RegistrationData.End:
        return end_registration(chat_id)


# Строки для взаимодействия с пользователем
def get_registration_message(message) -> Optional[str]:
    chat_id = message.chat.id

    if chat_id not in students:
        return add_data_to_user(chat_id, message.text, RegistrationData.Empty)
    if students[chat_id].name is None:
        return add_data_to_user(chat_id, message.text, RegistrationData.Name)
    if students[chat_id].surname is None:
        return add_data_to_user(chat_id, message.text, RegistrationData.Surname)
    if students[chat_id].lastname is None:
        return add_data_to_user(chat_id, message.text, RegistrationData.Patronymic)
    if not students[chat_id].is_added_program:
        return add_data_to_user(chat_id, message.text, RegistrationData.Program_Info)
    if message.text == 'Завершить регистрацию':
        return add_data_to_user(chat_id, message.text, RegistrationData.End)

    return add_data_to_user(chat_id, message.text, RegistrationData.University_Name)
