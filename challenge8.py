# "Remember that the problem with ECB is that it is stateless and deterministic; the same 16 byte plaintext block will always produce the same 16 byte ciphertext."
# This means that we need to find any duplicates blocks in a given line to find out which one is using ECB

def detectEcb(text_file) -> int:
    blocksize = 16
    for i, line in enumerate(text_file):

        # range starts at 0, stops at the line length and steps the blocksize amout
        blocks = [line[j:j+blocksize] for j in range(0, len(line), blocksize)]

        # since sets contain only *UNIQUE* values, if the blocks LIST has a different size than a set
        # created from it, it means it has multiple equal blocks in the line
        if len(blocks) != len(set(blocks)):
            return i
    return -1

with open("./res/8.txt", "rb") as f:
    text_file = f.readlines()

ecb_line = detectEcb(text_file)

if ecb_line == -1:
    print("No ECB encrypted line found.")
else:
    print("The line %d was encrypted using ECB." %(ecb_line))
