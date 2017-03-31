import re

def extract_punctuation(text):
    new_text = []
    for word in text:
        m = re.split('(\W+)',word)
        m = list(filter(None, m))
        new_text.extend(m)
    return new_text

def Translate(sentence):
       #algorithm to translate from english to pig latin
       #based on the rules set in wikipedia
       
       #all possible double consonants
       lst = ['sh', 'gl', 'ch', 'ph', 'tr', 'br', 'fr', 'bl', 'gr', 'st', 'sl', 'cl', 'pl', 'fl']
       sentence = re.split('( )',sentence)
       sentence = extract_punctuation(sentence)
       for k in range(len(sentence)):
               i = sentence[k]
               # Do nothing with punctuation
               if re.match('\W+',i) != None:
                      sentence[k] == i
               #Rule number 3 in wikipedia
               elif i[0] in ['a', 'e', 'i', 'o', 'u']:
                       sentence[k] = i+'way'
               #Rule number 2
               elif t(i) in lst:
                       sentence[k] = i[2:]+i[:2]+'ay'
               #rule number 1
               elif i.isalpha() == False:
                       sentence[k] = i
               else:
                       sentence[k] = i[1:]+i[0]+'ay'
       return ''.join(sentence)

def readfile(filename):
    #read local file stating a path relative to the current working directory
    try:
        F = open(filename, "r")
        return F.read()
    except OSError as err:
        return "ERROR_READING_FILE"

def t(str):
       #appending. Auxiliary function for the Translate function
       return str[0]+str[1]


if __name__ == "__main__":
       english_sentence = input('If you want to read from a file type "file " and the filename. Otherwise, type what you would like translated into pig-latin and press ENTER: ')
       print("English: " + english_sentence)
       #case the user type file first and then the path
       if (english_sentence.partition('file ')[2] != ""):
           english_sentence = readfile(english_sentence.partition('file ')[2])
       #making the translation
       
       pig_sentence = Translate(english_sentence)
       print("Latin Pig: " + pig_sentence)
