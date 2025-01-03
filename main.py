import sys
from password.generator_factory import PasswordGeneratorFactory

def main():
    while True:
        print("Password Generator")
        print("===================")
        print("1. Simple Password")
        print("2. Complex Password")
        print("3. Exit")
        choice = input("Choose the type of password: ")

        if choice == '3':
            sys.exit()

        if choice not in ['1', '2']:
            print("Invalid choice, please try again.")
            continue

        try:
            length = int(input("Enter the length of the password: "))
        except ValueError:
            print("Invalid length, please enter a number.")
            continue

        generator_type = 'simple' if choice == '1' else 'complex'
        generator = PasswordGeneratorFactory.create_generator(generator_type, length)
        password = generator.generate()
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
