import db

def display_pet_reel():
    pet_reel = db.select_all("SELECT pets.*, users.user_name FROM pets JOIN users ON users.id = pets.user_id;")
    return pet_reel

def insert_pet(name, type, image_url, favourite_food, username):
    user_id = db.select_one("SELECT id FROM users WHERE user_name = %s", [username])['id']
    db.insert(
        "INSERT INTO pets (name, type, image_url, favourite_food, user_id) VALUES (%s, %s, %s, %s, %s)",
        (name, type, image_url, favourite_food, int(user_id))
    )
    
def display_pet_reel_user(user_name):
    pet_reel_user = db.select_all_pets ("SELECT pets.*  FROM pets JOIN users ON users.id = pets.user_id Where user_name = %s;", [user_name])
    return pet_reel_user
    
 


