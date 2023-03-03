import db

def display_pet_reel():
    pet_reel = db.select_all("SELECT pets.*, users.user_name FROM pets JOIN users ON users.id = pets.user_id;")
    return pet_reel

def heart_counter(pet_id):
  
    db.update(
        "UPDATE pets SET hearts = hearts + 1 WHERE id = %s;",
        (pet_id,)
    )





