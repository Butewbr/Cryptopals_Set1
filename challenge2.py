inp1 = bytes.fromhex('1c0111001f010100061a024b53535009181c')
inp2 = bytes.fromhex('686974207468652062756c6c277320657965')

def xor(a, b) -> bytes:
    result=[]
    zipado = zip(a,b)
    for c1, c2 in zipado:
        # print(type(c1))
        result.append(c1 ^ c2)
    return bytes(result)

print('Raw result: %s'%(xor(inp1, inp2)))
print('Hex result: %s'%(xor(inp1, inp2).hex()))