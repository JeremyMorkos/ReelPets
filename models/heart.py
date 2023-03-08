import db

def heart_counter(user_id,pet_id): 
    hearts = db.select_one ("SELECT id FROM user_hearts WHERE user_id = %s AND pet_id = %s;",[user_id, pet_id])

    if hearts:
        db.delete(
        "DELETE FROM user_hearts WHERE user_id = %s AND pet_id = %s",
        [user_id, pet_id]  
    ) 
        

    else :
        db.insert(
            "INSERT INTO user_hearts (user_id, pet_id ) VALUES (%s,%s)",
            [user_id, pet_id]
        )
    
    result = db.select_one("SELECT Count(*) FROM user_hearts WHERE user_hearts.pet_id = %s",[pet_id])
    num_hearts = result['count']
    
    return num_hearts
 
    
  

