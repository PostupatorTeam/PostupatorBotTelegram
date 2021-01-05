from config.config import universities


def is_validate_university(student, university):
    if not university in universities:
        return False
    count = 0
    for program in student.programs:
        if program.universityName == university:
            count += 1
    if count >= 3:
        return False
    return True