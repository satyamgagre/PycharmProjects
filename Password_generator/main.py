import random
import string

def generate_password(length):
    if length < 8:
        print("Password length too short. Setting to minimum length of 8.")
        length = 8

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("----- PASSWORD GENERATOR -----")
    try:
        length = int(input("Enter desired password length (minimum 8): "))
        password = generate_password(length)
        print("Your password is: ",password)
    except ValueError:
        print("Please enter a valid number.")

main()