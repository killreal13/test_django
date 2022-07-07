from hashlib import md5

print((md5('vk.com/id_123123/'.encode()).hexdigest()[:10]))
