import random
import string

def generate_random_password(length):
    # Define the set of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password by selecting characters randomly from the set
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Example usage: Generate a random password of length 12
random_password = generate_random_password(12)
print("Random Password:", random_password)
