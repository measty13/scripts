import unittest

from fizzbuzz import *

#TODO
# zeroDivisionError


#DIVISIBLE
class Divisible(unittest.TestCase):

    def test_divisible_positive_true(self):
        self.assertTrue(divisible(10, 5), "Should be True")

    def test_divisible_positive_false(self):
        self.assertFalse(divisible(10, 4), "Should be False")

    def test_divisible_negative_true(self):
        self.assertTrue(divisible(-10, 2), "Should be True")

    def test_divisible_negative_false(self):
        self.assertFalse(divisible(-5, 3), "Should be False")

    def test_divisible_zero(self):
        self.assertEqual(divisible(1, 0), ZeroDivisionError, "Should be ZeroDivisionError")


#FIZZBUZZ
class FizzBuzz(unittest.TestCase):
    
    def test_fizzBuzz(self):
        result = ["FizzBuzz",1,2,"Fizz",4,"Buzz"]
        self.assertEqual(fizzBuzz(0, 5, 3, 5), result ,('Should be ' + str(result)))

    def test_fizzBuzz_fizz_and_buzz(self):
        result = ["FizzBuzz",1,"Fizz",3,"FizzBuzz"]
        self.assertEqual(fizzBuzz(0,4,2,4), result, ("Should be "+ str(result)))

    def test_fizzBuzz_positive_negative(self):
        result = ["Buzz","Fizz",-1,"FizzBuzz",1,"Fizz","Buzz"]
        self.assertEqual(fizzBuzz(-3,3,2,3), result, "Should be " + str(result))

    def test_fizzBuzz_zero_trigger1(self):
        result = ZeroDivisionError
        self.assertEqual(fizzBuzz(-3,3,0,1), result, "Should be ZeroDivisionError")

    def test_fizzBuzz_zero_trigger2(self):
        result = ZeroDivisionError
        self.assertEqual(fizzBuzz(-3,3,1,0), result, "Should be ZeroDivisionError")


if __name__ == '__main__':
    unittest.main()

