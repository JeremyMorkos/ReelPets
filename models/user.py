import db

def load_user(user_name):
    user = db.select_one ("SELECT users.* FROM users Where user_name = %s",[user_name])
    return user
 
    
def signup_user(user_name, password_hash, image_url):
    db.insert(
        "INSERT INTO users (user_name,password_hash,image_url) VALUES (%s, %s, %s)",
        [user_name, password_hash, image_url]

    )

def update_profile(id,user_name,password_hash, image_url):
    db.update(
              "UPDATE users SET user_name = %s, password_hash = %s, image_url = %s WHERE id = %s",
              (user_name,password_hash,image_url,id)
    )

