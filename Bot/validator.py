from Bot.config import universities

def is_validate_university(user, university):
    if len(user.universities) == 5:
        return False
    if not university in universities:
        return False
    for univer in user.universities:
        if univer.name == university:
            return False
    return True