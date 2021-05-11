from rsa_encryption import *

sended_massage = []
with open('massage.txt', 'r') as file:
    for line in file:
        sended_massage.append(int(line))


with open('key.txt', 'r') as file:
    for line in file:
        data = line.split(' ')
    data = [int(x) for x in data]

secret_key = rsa_get_secret_key(*data, russian_alph_dict)
print(rsa_decode(sended_massage, secret_key["secret_key"], russian_alph_dict))
