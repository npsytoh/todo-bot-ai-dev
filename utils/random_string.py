from string import ascii_lowercase
from string import digits
from random import choice


def get_random_string(size: int, chars: str = ascii_lowercase + digits):
    return ''.join(choice(chars) for _ in range(size))