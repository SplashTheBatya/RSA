from rsa_encryption import *


p = 11
q = 17
e = 11

keys = rsa_set_keys(p, q, e, russian_alph_dict)
massage = input("Введите сообщение: ")
encoded_massage = rsa_encode(massage, keys["open_key"], russian_alph_dict)

with open('massage.txt', 'w') as file:
    file.write('\n'.join(str(num) for num in encoded_massage))


sended_massage = []
with open('massage.txt', 'r') as file:
    for line in file:
        sended_massage.append(int(line))
print(rsa_decode(sended_massage, keys["secret_key"], russian_alph_dict))
