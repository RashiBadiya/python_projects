import string
import random

class Password:
    def __init__(self, charset, length):
        self.charset = charset
        self.length = length
        self.char_array = []

    def set_the_charset(self):
        if ('l' in self.charset):
            self.char_array.append(string.ascii_lowercase)
        if ('u' in self.charset):
            self.char_array.append(string.ascii_uppercase)
        if ('d' in self.charset):
            self.char_array.append(string.digits)
        if ('s' in self.charset):
            self.char_array.append(string.punctuation)

    def get_char_array(self):
        return self.char_array

    def generate_password(self):
        password = []
        for i in range(self.length):
            outer_index = random.randrange(0, len(self.char_array))
            inner_index = random.randrange(0, len(self.char_array[outer_index]))
            password.append(self.char_array[outer_index][inner_index])
        return ''.join(password)

if __name__ == "__main__":
    password = Password('ldu', 8)
    password.set_the_charset()
    generated_password = password.generate_password()
    print(generated_password)
