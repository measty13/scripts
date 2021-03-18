import unittest

from fizzbuzz import divisible, fizzBuzz

#TODO
# *write edge case tests for both functions


#DIVISIBLE
class Divisible(unittest.TestCase):

    def test_divisible(self):
        self.assertTrue(divisible(10, 5), "Should be True")


#FIZZBUZZ
class FizzBuzz(unittest.TestCase):
    
    def test_fizzBuzz(self):
        self.assertEqual(fizzBuzz(5, 3, 5),[1,2,"Fizz",4,"Buzz"],'Should be [1,2,"Fizz",4,"Buzz"]')


if __name__ == '__main__':
    unittest.main()

