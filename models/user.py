import db

def load_user(user_name):
    user = db.select_one ("SELECT users.* FROM users Where user_name = %s",[user_name])
    return user
    
def signup_user(user_name, password_hash):
    db.insert(
        "INSERT INTO users (user_name,password_hash) VALUES (%s, %s)",
        [user_name, password_hash]

    )
