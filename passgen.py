import random
import string


try:
    length = int(input("Enter the desired password length: "))
except ValueError:
    print("Invalid input. Please enter a number.")
    exit()


lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

all_chars = lowercase + uppercase + digits + symbols


password = ''.join(random.choice(all_chars) for _ in range(length))


print(f"Generated Password: {password}")
