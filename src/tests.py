import unittest
from pigtranslator import Translate

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
    

if __name__ == '__main__':
    unittest.main()