import sys,os
sys.path.append(os.path.join(os.path.dirname(os.curdir)))
from unittest import TestCase
from ..build import q07_randomsearch_predict
from inspect import getfullargspec

path = 'data/GermanData.csv'

AUC_Score = q07_randomsearch_predict(path)

class Test_randomsearch_predict(TestCase):
    def test_args(self):
        arg = getfullargspec(q07_randomsearch_predict).args
        self.assertEqual(len(arg), 1, "Expected argument(s) %d, Given %d" % (1, len(arg)))


    def test_AUC_Score(self):
        self.assertGreaterEqual(AUC_Score, 0.63,
                              "The Expected return value does not match with the given return value")
