import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def user():
    name = input("Your name: ")
    attempt = 3
    while attempt > 0:
        password = input("Enter password: ")
        special_characters = "!@#$%^&*()-_+=[]{}|;:,.<>?"
        lower = any(x.islower() for x in password)
        upper = any(x.isupper() for x in password)
        digits = any(x.isdigit() for x in password)
        character = any(char in special_characters for char in password )
        new_password = generate_password(8)
        if len(password) >= 8 and lower and upper and character and digits:
            print(f"{name} {password}")
        else:
            print(f"Password is weak.\nTry this password: {new_password} ")
            attempt -=1
user()
