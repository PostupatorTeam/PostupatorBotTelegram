from config.config import universities_list


def is_validate_university(student, university):
    if university not in universities_list:
        return False

    count = 0
    for program in student.programs:
        if program.university_name == university:
            count += 1

    return count < 3


def is_validate_message(message):
    allowed_characters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ- '

    for i in message:
        if i not in allowed_characters:
            return False

    return True
