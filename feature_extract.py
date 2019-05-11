from nltk.stem.porter import *


class Token():
    def __init__(self, word, pos, bio):
        self.token = word
        self.POS = pos
        self.BIO = bio

        self.previous_word = 'NULL'
        self.previous_pos = 'NULL'

        self.following_word = 'NULL'
        self.following_pos = 'NULL'

        self.previous_2_word = 'NULL'
        self.previous_2_pos = 'NULL'

        self.following_2_word = 'NULL'
        self.following_2_pos = 'NULL'



class Featuring():
    def __init__(self, token_list):
        self.token_list = token_list

    def update_attributes(self):
        for i in range(0, len(self.token_list)):
            token = self.token_list[i]
            if token.token == '' and self.token_list[i+1].token == '':
                break # Termination
            elif token.token == '':
                continue
            else:
                if self.token_list[i-1].token == '':
                    token.previous_word = 'Begin_of_Sent'
                    token.previous_pos = 'Begin_of_Sent'
                    token.previous_2_pos = 'Begin_of_Sent'
                    token.previous_2_word = 'Begin_of_Sent'
                else:
                    token.previous_word = self.token_list[i-1].token
                    token.previous_pos = self.token_list[i-1].POS
                    if self.token_list[i-2].token == '':
                        token.previous_2_pos = 'Begin_of_Sent'
                        token.previous_2_word = 'Begin_of_Sent'
                    else:
                        token.previous_2_pos = self.token_list[i-2].POS
                        token.previous_2_word = self.token_list[i-2].token

                if self.token_list[i+1].token == '':
                    token.following_word = 'End_of_Sent'
                    token.following_pos = 'End_of_Sent'
                    token.following_2_word = 'End_of_Sent'
                    token.following_2_pos = 'End_of_Sent'
                else:
                    token.following_word = self.token_list[i+1].token
                    token.following_pos = self.token_list[i+1].POS
                    if self.token_list[i+2].token == '':
                        token.following_2_pos = 'Begin_of_Sent'
                        token.following_2_word = 'Begin_of_Sent'
                    else:
                        token.following_2_pos = self.token_list[i-2].POS
                        token.following_2_word = self.token_list[i-2].token

        return

    def output(self, filename):
        file = open(filename, 'w')

        for token in self.token_list:

            if token.token == '':
                file.write('\n')
            else:
                str = token.token + '\t'+'pos='+token.POS + '\t'+\
                      'previous_word='+token.previous_word + '\t'+'previous_pos='+token.previous_pos + '\t'+\
                      'previous_2_word='+token.previous_2_word + '\t'+'previous_2_pos='+token.previous_2_pos + '\t'+\
                      'following_word='+token.following_word + '\t'+'following_pos='+token.following_pos + '\t'+\
                      'following_2_word='+ token.following_2_word + '\t' + 'following_2_pos=' + token.following_2_pos
                if token.BIO == '':
                    str += '\n'
                    file.write(str)
                else:
                    str += '\t' + token.BIO + '\n'
                    file.write(str)
                # if filename == 'test.feature':
                #     print(str)
        file.close()

def main():
    file = open('WSJ_02-21.pos-chunk', 'r')
    input_list = file.read().split('\n')
    file.close()

    token_list = []
    for token in input_list:
        if token == '':
            token_list.append(Token('', '', ''))
        else:
            temp = token.split()
            #print('The length of temp_list is,', temp.__len__())
            token_list.append(Token(temp[0], temp[1], temp[2]))
    print('token_list generated...')
    process = Featuring(token_list)
    print('featuring set up...')
    process.update_attributes()
    print('attributes updated...')
    process.output('training.feature')
    print('training feature done...')


    file = open('WSJ_23.pos', 'r')
    input_list = file.read().split('\n')
    file.close()

    token_list = []
    for token in input_list:
        if token == '':
            token_list.append(Token('', '', ''))
        else:
            temp = token.split()
            #print(temp)
            #print('The length of temp_list is,', temp.__len__())
            token_list.append(Token(temp[0], temp[1], ''))

    print('token_list generated...')
    process = Featuring(token_list)
    print('featuring set up...')
    process.update_attributes()
    print('attributes updated...')
    process.output('test.feature')
    print('training feature done...')


main()