import db

def load_user(user_name):
    user = db.select_one ("SELECT users.* FROM users Where user_name = %s",[user_name])
    return user
    