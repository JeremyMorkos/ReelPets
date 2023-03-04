from flask import (
    Flask,
    render_template,
    redirect, 
    request,
    session,
    flash 
)

from werkzeug.security import generate_password_hash, check_password_hash
from models.pet import display_pet_reel, heart_counter, insert_pet, display_pet_reel_user
from models.user import load_user, signup_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"



@app.route('/')
def index():
    pet_reel = display_pet_reel()
    return render_template('home.html', pet_reel=pet_reel)

@app.post('/hearts')
def heart_pet_post():
    if 'name' in session:
        pet_id = request.form.get('pet_id')
        heart_counter(pet_id)
        return redirect('/')
    else:
        flash('Sorry only memebers can love pets!', 'error')
        return redirect('login')
    
@app.get('/signup')
def signup_get():
    return render_template('signup.html')

@app.post('/signup')
def signup_post():
    user_name = request.form.get('user_name')
    password = request.form.get('password')
    password_hash = generate_password_hash(password)
    password_check = request.form.get('password_check')

    if password != password_check:
        flash('Passwords dont match', 'error')
        return render_template('signup.html')
    
    else:
        signup_user(user_name,password_hash)
        return redirect('/login')

@app.get('/login')
def login_get():
    if 'name' in session :
        return redirect('/')
    else:
        return render_template('login.html')

@app.post('/login')
def login_post():
    user_name = request.form.get('user_name')
    password = request.form.get('password')
    user = load_user(user_name)

    if user and check_password_hash(user['password_hash'], password):
        session['name'] = user_name
        return redirect('/')
    else:
        flash('Information is incorrect', 'error')
        return render_template('login.html')
        
@app.get('/profile')
def profile_get():

    if 'name' not in session:
        flash('Sorry only members can add pets!', 'error')
        return redirect('/')
    else:
        user_pet = display_pet_reel_user(session['name'])
        return render_template('profile.html',user_pet=user_pet)
    
@app.post('/profile')
def profile_post():
            
            user_id = session['name'] 
            name = request.form.get('name')
            type = request.form.get('type')
            image_url = request.form.get('image_url')
            favourite_food = request.form.get('favourite_food')
            insert_pet(name,type,image_url,favourite_food,user_id)
            return render_template('profile.html')
  

@app.route('/logout')
def logout():
    session.pop('name', None)
    return redirect('/')




if __name__ == "__main__":
    app.run(debug = True)