import random
import string

def generate_password(length):
    if length < 4:
        return "password should be at least 4 characters long."
    
    characters = string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(characters)for _ in range(length))
    return password

try:
    length=int(input("enter password length=" ))
    print("generate password=",generate_password (length))
except valueError:
    print("please enter a valid password.")



