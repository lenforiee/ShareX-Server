import math
import random
import string


def random_str(rounds: int = 8):
    return "".join(
        [
            random.choice(
                string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase
            )
            for _ in range(rounds)
        ]
    )


def convert_size(file_size: int):

    if not file_size:
        return "0B"

    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    megabytes = int(math.floor(math.log(file_size, 1024)))
    rest = math.pow(1024, megabytes)
    size = round(file_size / rest, 2)
    return f"{size}{size_name[megabytes]}"


def safe_username(s: str):
    return s.rstrip().replace(" ", "_").lower()
