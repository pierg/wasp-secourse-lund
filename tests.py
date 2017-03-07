import unittest
from src.pigtranslator import Translate
from src.pigtranslator import readfile


class TestTranslate(unittest.TestCase):
    #For rule 1 in Wikipedia
    def test_consonantSounds(self):
        s = 'pig'
        self.assertEqual(Translate(s), 'igpay')

    #For rule 2 in Wikipedia
    def test_consonantClusters(self):
         s = 'cheers'
         self.assertEqual(Translate(s), 'eerschay')
    
    #For rule 3 in Wikipedia
    def test_vowelSounds(self):
         s = 'eat'
         self.assertEqual(Translate(s), 'eatway')

    # To test file feature
    def test_file_success(self):
        s = './test_files/test0.txt'
        self.assertEqual(readfile(s), 'Once upon a time there was a pig walking around in a dark forest.\nSuddenly, it met a scary cow that spoke in a strange language.')

    #To test file errors
    def test_file_error(self) :
        s = 'ooohhlala'
        self.assertEqual(readfile(s), "ERROR_READING_FILE")

if __name__ == '__main__':
    unittest.main()