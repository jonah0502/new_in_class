  
import unittest


class TestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual(code.isLY(2000), True)
    def test_2(self):
        self.assertEqual(code.isLY(1999), False)
    @unittest.expectedFailure
    def test_3(self):
        self.assertEqual(code.isLY(1999), True)



if __name__ == "__main__":
    unittest.main(verbosity=2)