from Crypto.Cipher import AES
from base64 import b64decode

with open('./res/7.txt') as f:
    file_data = f.read()

text_file = b64decode(file_data)
key = b'YELLOW SUBMARINE'

cryptographed_text = AES.new(key, AES.MODE_ECB)

decoded_text = cryptographed_text.decrypt(text_file)

print(decoded_text.decode('ascii'))