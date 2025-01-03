import random
import string

class PasswordGenerator:
    def generate(self):
        raise NotImplementedError("Subclasses should implement this!")

class SimplePasswordGenerator(PasswordGenerator):
    def __init__(self, length):
        self.length = length
        self.charset = string.ascii_letters

    def generate(self):
        return ''.join(random.choice(self.charset) for _ in range(self.length))

class ComplexPasswordGenerator(PasswordGenerator):
    def __init__(self, length):
        self.length = length
        self.charset = string.ascii_letters + string.digits + string.punctuation

    def generate(self):
        return ''.join(random.choice(self.charset) for _ in range(self.length))
