from flask import (
    Flask,
    render_template,
    redirect, 
    request,
    session,
    flash 
)
from cloudinary import CloudinaryImage
import cloudinary.uploader
from werkzeug.security import generate_password_hash, check_password_hash
from models.pet import display_pet_reel, insert_pet, display_pet_reel_user,delete_pet, select_one_pet,update_image
from models.user import load_user, signup_user,update_password,update_pofile_picture
from models.heart import heart_counter

app = Flask(__name__)

app.config['SECRET_KEY'] = 'super secret key'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


@app.route('/')
def index():
    print(session)
    if 'name' in session:
        user_name = session['name']
        user = load_user(user_name)
        image_url = user['image_url']
    else:
        image_url = None
    pet_reel = display_pet_reel()
    return render_template('home.html', pet_reel=pet_reel,image_url=image_url)

    
@app.get('/signup')
def signup_get():
    return render_template('signup.html')

@app.post('/signup')
def signup_post():
    user_name = request.form.get('user_name')
    password = request.form.get('password')
    image = request.files.get('image')   

    if not image:
        flash('No image file provided', 'error')
        return redirect('/signup')

    upload_image = cloudinary.uploader.upload(image)
    image_url = upload_image['url']
    
    password_hash = generate_password_hash(password)
    password_check = request.form.get('password_check')

    if password != password_check:
        flash('Passwords dont match', 'error')
        return render_template('signup.html')
    
    else:
        signup_user(user_name,password_hash, image_url)
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
        session['id'] = user['id']
        print(user['id'])
        return redirect('/')
    else:
        flash('Login information is incorrect, try again!', 'error')
        return render_template('login.html')
    
@app.post('/hearts')
def heart_pet_post():
    user_id = session['id']
    pet_id = request.args.get('pet_id')
    num_hearts = heart_counter(user_id, pet_id)

    return {
            "num_hearts": num_hearts
        }

@app.get('/profile')
def profile_get(): 
    user_name = session['name']
    user = load_user(user_name)
    image_url = user['image_url']
    user_pet = display_pet_reel_user(session['name'])
    return render_template('profile.html',user_pet=user_pet, image_url=image_url)
    
@app.post('/profile') 
def profile_post():
    user_id = session['name'] 
    name = request.form.get('name')
    type = request.form.get('type')
    image = request.files.get('image')
    favourite_food = request.form.get('favourite_food')
    upload_image = cloudinary.uploader.upload(image)
    image_url = upload_image['url']
    insert_pet(name,type,image_url,favourite_food,user_id)
    return redirect('/profile')
  
@app.get('/edit_password')
def edit_password_get():
    user_name = session['name']
    user = load_user(user_name)
    image_url = user['image_url']
    return render_template('edit_password.html',image_url=image_url)

@app.post('/edit_password')
def edit_password_post():
    user_id = session['id']
    password = request.form.get('password')
    password_hash = generate_password_hash(password)
    password_check = request.form.get('password_check')

    if password != password_check:
        flash('Passwords dont match', 'error')
        return render_template('edit_password.html')
    else:
         update_password(user_id,password_hash)
         return redirect('/profile')

@app.get('/edit_profile_picture')
def edit_profile_picture_get():
    user_name = session['name']
    user = load_user(user_name)
    image_url = user['image_url']
    return render_template('edit_profile_picture.html',image_url=image_url)

@app.post('/edit_profile_picture')
def edit_profile_picture_post():
    user_id = session['id']
    image = request.files.get('image')    
    upload_image = cloudinary.uploader.upload(image)
    image_url = upload_image['url']
    
    update_pofile_picture(user_id,image_url)
    return redirect('/profile')
 
@app.get('/edit_pet_picture/<pet_id>')
def edit_pet_picture_get(pet_id):
    pet = select_one_pet(pet_id)
    user_name = session['name']
    user = load_user(user_name)
    image_url = user['image_url']
    return render_template('edit_pet_picture.html',pet=pet,image_url=image_url)

@app.post('/add_frame')
def add_frame():
    pet_id = request.form.get('pet_id')
    pet = select_one_pet(pet_id)
    link = pet['image_url']
    link = link.rsplit('/', 1)[-1]
    image_url = CloudinaryImage(link).build_url( width=450, radius=0, border="5px_solid_rgb:000000")
    update_image(pet_id,image_url)
    return redirect("/profile")

@app.get('/about/<user_id>')
def view_user_profile(user_id):
    
    if 'name' not in session:
        flash('Sorry only members can see profiles', 'error')
        return redirect('/')

    elif user_id == session['name']:
         return redirect('/profile')
     
    elif  'name' in session:
        user_name = session['name']
        user = load_user(user_name)
        image_url = user['image_url']
        user_pet = display_pet_reel_user(user_id)
        return render_template('about.html', user_pet=user_pet,user_id=user_id,image_url=image_url)


@app.get('/logout')
def logout():
    session.pop('name', None)
    session.pop('id', None)
    return redirect('/')

@app.get('/delete')
def delete_user_pet_get():
    pet_id = request.args.get('id')
    pet = select_one_pet(pet_id)
    return render_template('delete.html',  pet=pet)


@app.post('/delete')
def delete_user_pet_post():
    pet_id = request.form.get('id')
    delete_pet(pet_id)
    return redirect('/profile')

if __name__ == "__main__":
    app.run(debug = True)