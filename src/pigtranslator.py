def Translate(sentence):
       lst = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']
       sentence = sentence.split()
       for k in range(len(sentence)):
               i = sentence[k]
               if i[0] in ['a', 'e', 'i', 'o', 'u']:
                       sentence[k] = i+'ay'
               elif t(i) in lst:
                       sentence[k] = i[2:]+i[:2]+'ay'
               elif i.isalpha() == False:
                       sentence[k] = i
               else:
                       sentence[k] = i[1:]+i[0]+'ay'
       return ' '.join(sentence)

def t(str):
       return str[0]+str[1]

if __name__ == "__main__":
       english_sentence = input('Type what you would like translated into pig-latin and press ENTER: ')
       print(english_sentence)
       pig_sentence = Translate(english_sentence)
       print(pig_sentence)