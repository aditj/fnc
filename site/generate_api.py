import random
import string

def generate_api(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
