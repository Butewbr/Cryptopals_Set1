# File created to define variables and functions for the challenges 3 and 4
ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def singleXor(a, b) -> bytes:
    result=[]
    for char in a:
        result.append(char ^ b)
    return bytes(result)

def tryDecoding(line) -> dict:
    dec_dict = {}
    # in this for loop, the line is decoded with each letter of the ascii string
    for i in range(256):
        dec_dict[chr(i)] = singleXor(line, i)
    # then, the dictionary with all the decoded options is returned
    return dec_dict

def scoreAnswers(d) -> dict:
    scores = {}
    for letter, answer in d.items():
        answer_score = 0.0
        for character in str(answer):
            if character in letter_freq_dict:
                # every letter that is contained in the frequency dictionary adds value to the score
                answer_score += letter_freq_dict[character]
            elif character == ' ':
                answer_score += 2
            else:
                # every letter that is not in the frequency dictionary and it is not the 'space' character decreases the answer score
                answer_score -= 3
        scores[letter] = [answer_score, answer]
    return dict(sorted(scores.items(), key=lambda item: item[1][0], reverse=True))

def getBest(d, num = 5) -> dict:
    best_ans = {}
    i = 0
    for letter, score_ans in d.items():
        best_ans[letter] = [score_ans[0], score_ans[1]]

        i+=1
        if(i >= num):
            break    
    return best_ans

# Creating the letter frequency dictionary

# list available in http://corpus.leeds.ac.uk/frqc/internet-en.num
# first open the file
text_file = open("./res/internet-en-forms.num.txt")


# create a list of all tuples in the document with each word and their respective rank and normalised frequency
word = []
letter = []
i=0
# then create a dict for each letter and it's frequency
letter_freq_dict = {}
for line in text_file:
    word.append(line.split())

    for letter in word[i][2]:
        if letter in letter_freq_dict:
            letter_freq_dict[letter] += float(word[i][1])/400000
        else:
            letter_freq_dict[letter] = float(word[i][1])/400000
    i+=1   
    # we can use the normalised frequency to weight each word accordantly with how common they are
    # with that, we can count each letter in each word, ranking which letters are most common
    # based on the most used words in the English language in the Internet

# it is important to point out that this letter ranking is given by the frequency of *used* letters
# and not how frequently they are present in the English vocabulary

letter_freq_dict = dict(sorted(letter_freq_dict.items(), key=lambda item: item[1], reverse=True))

# removing any character that is not in the ascii letters string will return a better result:

letters_to_remove = []
for letter in letter_freq_dict.keys():
    if letter not in ascii_letters and letter != "\'":
        letters_to_remove.append(letter)

for letter in letters_to_remove:
    letter_freq_dict.pop(letter)

if __name__ == "__main__":
    inp1 = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

    decoded_dict = tryDecoding(inp1)

    # now that we have a list of possible answers, we may score which of final strings has more common characters. This will be useful to filter out noisy answers

    scored_answers = scoreAnswers(decoded_dict)

    # now we have a dictionary with all the decoded answers scored.

    # with the function getBest, we can select how many tries to show with the second argument:
    # it is 5 by default
    best_results = getBest(scored_answers, 1)
    for letter, score_ans in best_results.items():
            print('Decoded using the character \'%s\' (ASCII: %d) with a score of %.3f: %s' %(letter, ord(letter), score_ans[0], score_ans[1]))

    # this shows that the right key for decoding is X (uppercase x)