from base_coder import *
import numpy as np

a = ord('а')
rus_char = ''.join([chr(i) for i in range(a, a + 6)] + [chr(a + 33)] + [chr(i) for i in range(a + 6, a + 32)])
special_char = {33: '.', 34: ',', 35: ' ', 36: '?'}

russian_alph_dict = dict(list(enumerate(rus_char)))
russian_alph_dict.update(special_char)


def is_prime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


def euler_func(p: int, q: int):
    return (p - 1) * (q - 1)


def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def rsa_set_open_key(p: int, q: int, e: int, encoding_dict: dict):
    if not is_prime(p) or not is_prime(q):
        raise ValueError("p и q должны быть простыми")
    phi = euler_func(p, q)
    if not is_prime(e):
        raise ValueError("e должно быть простым числом ")
    elif e >= phi:
        raise ValueError("e должно быть быть меньше phi")
    elif np.gcd(phi, e) != 1:
        raise ValueError("e должно быть взаимно простым с phi")
    else:
        n = abs(p * q)
        if n < len(encoding_dict):
            raise ValueError("mod(p * q) должен быть больше чем длина словаря языка шифрования")
        open_key = {"e": e, "n": n}

    return {"open_key": open_key}


def rsa_get_secret_key(p: int, q: int, e: int, encoding_dict: dict):
    if not is_prime(p) or not is_prime(q):
        raise ValueError("p и q должны быть простыми")
    phi = euler_func(p, q)
    if not is_prime(e):
        raise ValueError("e должно быть простым числом ")
    elif e >= phi:
        raise ValueError("e должно быть быть меньше phi")
    elif np.gcd(phi, e) != 1:
        raise ValueError("e должно быть взаимно простым с phi")
    else:
        gcd, x, y = gcd_extended(e, phi)
        d = (x % phi + phi) % phi
        n = abs(p * q)
        secret_key = {"d": d, "n": n}

    return {"secret_key": secret_key}


def rsa_encode(massage: str, open_key: dict, encoding_dict: dict):
    massage_numeric_list = coder(list(massage.lower()), encoding_dict)
    massage_encoded_numeric_list = []
    for word_num in massage_numeric_list:
        number = (word_num ** open_key["e"]) % open_key["n"]
        massage_encoded_numeric_list.append(number)

    return massage_encoded_numeric_list


def rsa_decode(encoded_numeric_list: list, secret_key: dict, encoding_dict: dict):
    decoded_numeric_list = []
    for num in encoded_numeric_list:
        encoded_num = num ** secret_key["d"] % secret_key["n"]
        decoded_numeric_list.append(encoded_num)

    massage_list = decoder(decoded_numeric_list, encoding_dict)

    return ''.join(massage_list)
