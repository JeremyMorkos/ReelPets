import db

def load_user(user_name):
    user = db.select_one ("SELECT users.* FROM users Where user_name = %s",[user_name])
    return user
 
    
def signup_user(user_name, password_hash, image_url):
    db.insert(
        "INSERT INTO users (user_name,password_hash,image_url) VALUES (%s, %s, %s)",
        [user_name, password_hash, image_url]

    )

def update_password(id,password_hash):
    db.update(
              "UPDATE users SET password_hash = %s WHERE id = %s",
              (password_hash,id)
    )

def update_pofile_picture(id,image_url):
    db.update(
              "UPDATE users SET image_url = %s WHERE id = %s",
              (image_url,id)
    )




