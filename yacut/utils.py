import random
import string

from .constants import SHORT_AUTO_MAX_LENGTH
from .models import URLMap


def generate_short_url():
    while True:
        short = ''.join(
            random.choices(
                string.ascii_letters + string.digits, k=SHORT_AUTO_MAX_LENGTH
            )
        )
        if URLMap.query.filter_by(short=short).first() is None:
            break
    return short
