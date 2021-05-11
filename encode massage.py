from rsa_encryption import *

p = 11
q = 17
e = 11

open_key = rsa_set_open_key(p, q, e, russian_alph_dict)
massage = input("Введите сообщение: ")
encoded_massage = rsa_encode(massage, open_key["open_key"], russian_alph_dict)

with open('massage.txt', 'w') as file:
    file.write('\n'.join(str(num) for num in encoded_massage))


with open('key.txt', 'w') as file:
    file.write(str(p) + ' ')
    file.write(str(q) + ' ')
    file.write(str(e))