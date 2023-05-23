import random

# Character List
alphabet_min = "abcdefghijklmnopqrstuvwxyz"
alphabet_may = alphabet_min.upper()
symbols = '.,:;\'-_@"/\\#[](){}<>~*+=&%¿?¡!$'
numbers = '0123456789'
full_characters = alphabet_min + alphabet_may + numbers + symbols


def password_generator(pwd_size):
    selected_characters = random.sample(full_characters, pwd_size)
    password_created = "".join(selected_characters)
    return password_created
