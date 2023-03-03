from flask import (
    Flask,
    render_template,
    redirect, 
    request,
    session 
)
from werkzeug.security import check_password_hash
from models.pet import display_pet_reel, heart_counter
from models.user import load_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


# if __name__ == "__main__":
#     app.run(debug = True)


@app.route('/')
def index():
    pet_reel = display_pet_reel()
    return render_template('home.html', pet_reel=pet_reel)

@app.post('/hearts')
def heart_pet_post():
    pet_id = request.form.get('pet_id')
    heart_counter(pet_id)
    return redirect('/')

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
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('name', None)
    return redirect('/')


