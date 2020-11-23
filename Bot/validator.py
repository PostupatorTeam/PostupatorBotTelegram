import Bot.userManager
from Bot.config import universities

def validate_university(id,university):
    if len(Bot.userManager.users[id].universities) == 5:
        return False
    if not university in universities:
        return False
    if university in Bot.userManager.users[id].universities:
        return False
    return True