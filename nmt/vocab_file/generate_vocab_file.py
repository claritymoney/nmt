import string


char_list = sorted(list(set(string.printable.lower())))
char_list = ['<unk>','<s>','</s>'] + char_list[5:]
with open('/tmp/nmt_model/vocab/char_vocab_file.txt', 'w') as f:
    for char in char_list:
        f.write(char)
        f.write('\n')
print('done')




