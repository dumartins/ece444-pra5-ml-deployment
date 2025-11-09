import unittest
from application import _predict_text

# run with python -m unittest application_test.py

class Test(unittest.TestCase):
    def test_one(self):
        sample_news = 'Cristiano Ronaldo is a volleyball player.'
        prediction = _predict_text(sample_news)
        self.assertEqual(prediction, 'FAKE')
    
    def test_two(self):
        sample_news = 'There is a new consensus in the scientific community that the earth is flat.'
        prediction = _predict_text(sample_news)
        self.assertEqual(prediction, 'FAKE')

    def test_three(self):
        sample_news = 'Germany won the 2014 FIFA World Cup after defeating Argentina 1-0 in the final.'
        prediction = _predict_text(sample_news)
        self.assertEqual(prediction, 'REAL')

    def test_four(self):
        sample_news = 'The Apollo 11 mission took place in 1969.'
        prediction = _predict_text(sample_news)
        self.assertEqual(prediction, 'REAL')
