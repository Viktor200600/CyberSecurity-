import base64
import random
import string
def generate_password(length: int = 10):
    alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits
    password = ''.join(random.choice(alphabet) for i in range(length))
    return password
def encrypt_pass(password):
    encoded_bytes = base64.b64encode(password.encode())  # кодуємо у Base64
    encoded_str = encoded_bytes.decode('utf-8')  # перетворюємо bytes у string
    return encoded_str  # повертаємо закодований результат

def decrypt_pass(encoded_password):
    try:
        decoded_bytes = base64.b64decode(encoded_password)  # декодуємо Base64
        decoded_str = decoded_bytes.decode('utf-8')  # перетворюємо bytes у string
        print("Decoded:", decoded_str)
    except Exception as e:
        print("Error during decoding:", e)



while True:
    usr_input = int(input(" 1 generate password\n 2 encrypt password\n 3 decrypt password\n 4 exit\n Enter a number:"))
    if usr_input == 1:
        kek = generate_password()
        print(kek)
    elif usr_input == 2:
        encoded = encrypt_pass(password=kek)
        print(encoded)
    elif usr_input == 3:
        decrypt_pass(encoded)
    elif usr_input == 4:
        break

