import unittest
from pigtranslator import Translate

class TestTranslate(unittest.TestCase):

    def test_consonantSounds(self):
        s = 'pig'
        self.assertEqual(Translate(s), 'igpay')

    def test_consonantClusters(self):
         s = 'cheers'
         self.assertEqual(Translate(s), 'eerschay')
         
    def test_vowelSounds(self):
         s = 'eat'
         self.assertEqual(Translate(s), 'eatway')
    

if __name__ == '__main__':
    unittest.main()