from pigtranslator import *

if __name__ == "__main__":
       english_sentence = input('Type what you would like translated into pig-latin and press ENTER: ')
       print(english_sentence)
       pig_sentence = Translate(english_sentence)
       print(pig_sentence)