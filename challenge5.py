def singleCharXor(a, b) -> bytes:
    result=chr(a ^ b)
    return bytes(result, 'utf-8')

def repeatingKeyDecriptor(text, key, turnHex = True) -> bytes:
    i=0
    if turnHex:
        result_array = ''
        for char in text:
            result_array += bytes.hex(singleCharXor(char, key[i]))
            i+=1
            if i==len(key):
                i=0
    else:
        result_array = bytearray()
        for char in text:
            result_array += singleCharXor(char, key[i])
            i+=1
            if i==len(key):
                i=0
            
    return result_array

if __name__ == "__main__":
    inp = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    key = b'ICE'
    print((repeatingKeyDecriptor(inp, key, True)))
    if((repeatingKeyDecriptor(inp, key, True)) == '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'):
        print('tá certo')