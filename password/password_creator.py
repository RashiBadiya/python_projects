from random_password_creator import Password

if __name__ == "__main__":
    charset = input(
        "Enter the character set ('l' for lowercase, 'u' for uppercase, 'd' for digits, 's' for special characters): ")
    length = int(input("Enter the password length: "))

    password = Password(charset, length)
    password.set_the_charset()
    generated_password = password.generate_password()
    print("Generated Password:", generated_password)
