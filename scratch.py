from werkzeug.security import generate_password_hash

password = generate_password_hash('goodbye')
print(password)