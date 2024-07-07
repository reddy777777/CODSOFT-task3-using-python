import string
import random


def generate_password(length):
    # Define possible characters for the password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    while True:
        try:
            length = int(input("Enter the desired length for the password: "))
            if length <= 0:
                print("Please enter a positive integer for the length.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        password = generate_password(length)
        print(f"Generated Password: {password}\n")

        another = input("Generate another password? (yes/no): ").lower()
        if another != 'yes':
            break

# Run the main function
main()