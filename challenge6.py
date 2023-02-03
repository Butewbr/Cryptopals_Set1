from base64 import b64decode
from challenge3 import tryDecoding, scoreAnswers, getBest
from challenge5 import repeatingKeyDecriptor
            
def hammingDistanceCalculator(a, b) -> int:
    inputs_zipados = zip(a,b)

    soma=0
    for byte1, byte2 in inputs_zipados:
        soma+=bin(byte1 ^ byte2).count('1')
        # the '1's that remain from a XOR operation means the bits differed in that coordinate (exclusive or)
    return soma

def keySizeTester(text) -> int:
    total_hamming = []
    for i in range(41):
        total_hamming += [hammingDistanceCalculator(text[-i:] + text[:-i], text)]
        # with the -i: and :-i the line is being moved left and right by 'i' to check the hamming between the texts

    return total_hamming.index(min(total_hamming[1:])) 
    # starts in 1 since the [0] will always be 0
    # it will search with the 'min' method to find in which index, in this case, the key size, has the overall
    # lowest hamming distance

def getKey(text, key_size) -> bytes:
    key = b''
    for i in range(key_size):
        # this is the step 5, "break the ciphertext into chunk of KEYSIZE length."
        chunk = text[i:-1:key_size]
        key += bytes(list(getBest(scoreAnswers(tryDecoding(chunk)), 1).keys())[0], 'utf-8')
        # here we get every best scored keys using the same method of challenge 3 and attach it to the final key string.
        # when the loop finishes, we will have the full key
    return key

if __name__ == "__main__":

    with open('./res/6.txt') as f:
        file_data = f.read()

    text_file = b64decode(file_data.encode())

    size = keySizeTester(text_file)
    key = getKey(text_file, size)

    # print(key)
    print('The key to decript is: %s\nWith a size of %s' %(key, size))
    print(repeatingKeyDecriptor(text_file, key, False).decode('ascii'))