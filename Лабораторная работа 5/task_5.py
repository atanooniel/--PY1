import random
import string


def get_random_password(pass_len: int = 8) -> str:
    return "".join(random.sample((string.ascii_letters + string.digits), pass_len))


print(get_random_password())
