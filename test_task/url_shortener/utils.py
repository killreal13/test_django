from hashlib import md5


def shortener(domain: str, link: str) -> str:
    return md5(f'{domain} + {link}'.encode()).hexdigest()[:10]