import random
import string

def generate_password(length: int = 10):
    alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = ''.join(random.choice(alphabet) for i in range(length))
    return password
password = generate_password()
print(password)
