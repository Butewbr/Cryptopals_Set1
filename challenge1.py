from base64 import b64encode

inp = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
decoded = bytes.fromhex(inp)
result = b64encode(decoded)

print('Hex string: %s' %(inp))
print('Decoded string: %s' %(decoded))
print('Base 64 encoded string: %s' %(result))