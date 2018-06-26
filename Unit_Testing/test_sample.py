import unittest

from ..code.Sample import sample

class TestCase_001(unittest.TestCase):

    def setUp(self):
        pass

    #sample test
    #add description of what test does here
    def test__001(self):
        sampple = sample()
        self.assertEquals(sample.sample(), "this is a sample")

if __name__ == '__main__':
    unittest.main()