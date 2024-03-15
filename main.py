


name = input("Your name: ")
password = input("Enter password: ")

special_characters = "!@#$%^&*()-_+=[]{}|;:,.<>?"

if len(password) >= 8 and any(x.islower() for x in password) and any(x.isupper() for x in password) and any(char in special_characters for char in password):
    print(f"{name} {password}")
else:
    print("Password is weak.\nThis is your New Password: ")

