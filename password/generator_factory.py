from .generator import SimplePasswordGenerator, ComplexPasswordGenerator

class PasswordGeneratorFactory:
    @staticmethod
    def create_generator(generator_type, length):
        if generator_type == 'simple':
            return SimplePasswordGenerator(length)
        elif generator_type == 'complex':
            return ComplexPasswordGenerator(length)
        else:
            raise ValueError(f"Unknown generator type: {generator_type}")
