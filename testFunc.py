import unittest
import test

class TestTest(unittest.TestCase):
    #test add function
    def test_add(self):
        self.assertEqual(test.add(), 25)

if __name__ == '__main__':
    unittest.main()
