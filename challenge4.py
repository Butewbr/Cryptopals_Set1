from challenge3 import tryDecoding, scoreAnswers, getBest
text_file = open("./res/4.txt")

lines = text_file.read().split('\n')

i=1
best_dict = {}
for line in lines:
    list_of_decoded_line = tryDecoding(bytes.fromhex(line))
    scored_answer_in_line = scoreAnswers(list_of_decoded_line)

    cur_dict = getBest(scored_answer_in_line, 1)
    
    for letter, score_ans in cur_dict.items():
        best_dict[i] = [letter, score_ans[0], score_ans[1]]
    i+=1

i=1
cur_score = -1000
for line, (letter, score, answer) in best_dict.items():
    if cur_score < score:
        cur_score = score
        encoded_line=i   
    i+=1


final_answer = {encoded_line: best_dict[encoded_line]}

print('The line %d was the encoded string. It was cracked using the character \'%s\' (ASCII: %d) with a score of %.3f: %s' %(encoded_line, final_answer[encoded_line][0], ord(final_answer[encoded_line][0]), final_answer[encoded_line][1], final_answer[encoded_line][2]))