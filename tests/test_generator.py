import unittest
import string
from password.generator_factory import PasswordGeneratorFactory

class TestPasswordGenerators(unittest.TestCase):
    def test_simple_password_generator(self):
        generator = PasswordGeneratorFactory.create_generator('simple', 16)
        password = generator.generate()
        
        self.assertEqual(len(password), 16)
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isupper() for c in password))

    def test_complex_password_generator(self):
        generator = PasswordGeneratorFactory.create_generator('complex', 16)
        password = generator.generate()
        
        self.assertEqual(len(password), 16)
        self.assertTrue(any(c.islower() for c in password))
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        self.assertTrue(any(c in string.punctuation for c in password))

if __name__ == '__main__':
    unittest.main()