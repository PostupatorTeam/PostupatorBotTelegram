def insert_main_table(userid: str, name: str, surname: str, lastname: str, university: str) -> str:
    return f"""INSERT INTO main_table(userid, name, surname, lastname, university_name, notifications) 
                            VALUES ('{userid}', '{name}', '{surname}', '{lastname}', '{university}', false)"""


def insert_spbu_table(userid: str, educational_form: str, pay_form: str, program: str, place: int) -> str:
    return f"""INSERT INTO spbu_table(userid, educational_form, pay_form, program, place) 
                                VALUES ('{userid}', '{educational_form}', '{pay_form}', '{program}', {place})"""


def insert_ranepa_table(userid: str, departament: str, approval: str, form: str, program: str, place: int) -> str:
    return f"""INSERT INTO ranepa_table(userid, departament, approval, form, program, place) 
                                VALUES ('{userid}', '{departament}', '{approval}', '{form}', '{program}', {place})"""


def insert_etu_table(userid: str, form: str, program: str, place: int) -> str:
    return f"""INSERT INTO etu_table(userid, form, program, place) 
                                VALUES ('{userid}', '{form}', '{program}', {place})"""


def get_universities(userid: str) -> str:
    return f"""SELECT university_name FROM main_table WHERE userid='{userid}'"""


def delete_by_id(table_name: str, userid: str) -> str:
    return f"""DELETE FROM {table_name} WHERE userid='{userid}'"""


def get_info_by_id(table_name: str, userid: str) -> str:
    return f"""SELECT * FROM {table_name} WHERE userid='{userid}'"""


def get_info_by_id_and_notifications(userid: str, notifications: str) -> str:
    return f"""SELECT * FROM main_table WHERE userid='{userid}' and notifications={notifications}"""


def set_notifications(userid: str, notifications: str) -> str:
    return f"""UPDATE main_table SET notifications = {notifications} WHERE userid='{userid}'"""


def get_all_users_with_notifications() -> str:
    return f"""SELECT * FROM main_table WHERE notifications=true"""


def get_user_from_ranepa_table(userid: str, departament: str, approval: str, form: str, program: str) -> str:
    return f"""SELECT * FROM ranepa_table WHERE 
                                userid='{userid}' and departament='{departament}' and approval='{approval}' and 
                                form='{form}' and program='{program}'"""


def get_user_from_spbu_table(userid: str, educational_form: str, pay_form: str, program: str) -> str:
    return f"""SELECT * FROM spbu_table WHERE 
                                userid='{userid}' and educational_form='{educational_form}' and 
                                pay_form='{pay_form}' and program='{program}'"""


def get_user_from_etu_table(userid: str, form: str, program: str) -> str:
    return f"""SELECT * FROM etu_table WHERE userid='{userid}' and form='{form}' and program='{program}'"""


def set_place_in_ranepa_table(userid: str, departament: str, approval: str, form: str, program: str, place: int) -> str:
    return f"""UPDATE ranepa_table SET place = {place} WHERE 
                                                userid='{userid}' and departament='{departament}' and 
                                                approval='{approval}' and form='{form}' and program='{program}'"""


def set_place_in_spbu_table(userid: str, educational_form: str, pay_form: str, program: str, place: int) -> str:
    return f"""UPDATE spbu_table SET place = {place} WHERE 
                                userid='{userid}' and educational_form='{educational_form}' and 
                                pay_form='{pay_form}' and program='{program}'"""


def set_place_in_etu_table(userid: str, form: str, program: str, place) -> str:
    return f"""UPDATE etu_table SET place = {place} WHERE userid='{userid}' and form='{form}' and program='{program}'"""
