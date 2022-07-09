from hashlib import md5


def shortener(domain: str, link: str) -> str:
    return domain + md5(link.encode()).hexdigest()[:6]
