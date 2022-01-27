import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):

    name = []
    for i in range(number_of_small_letters):
        name.append(random.choice(string.ascii_lowercase))
    for i in range(number_of_capital_letters):
        name.append(random.choice(string.ascii_uppercase))
    for i in range(number_of_digits):
        name.append(str(random.randint(0, 9)))
    for i in range(number_of_special_chars):
        name.append(random.choice(allowed_special_chars))
    
    identity = random.sample(name, len(name))
    return ''.join(identity)

