##
# @file math_library_tests.py
# @brief Tests for mathematical functions
# @author Samuel Slávik
#

import unittest

##
# $brief Importing math functions from math_library
#
from math_library import MathFunctions
math = MathFunctions()

##
# @brief Defining class "Test" for all the tests
#
class Test(unittest.TestCase):

    ##
    # @brief Testing addition
    # Looping through pairs of testing numbers, passing them into given function
    # and comparing results with the expected ones.
    #
    def test_addition(self):
        ##
        # @brief Pairs of testing arguments
        #
        test_numbers = [[0, 0], [42, 23], [-42, -23], [42, 0], [0, -42],
                        [3.14, 42], [-42, 3.14], [11.9, 2.72], [14.88, -666.0]]
        ##
        # @brief Expected correct results
        #
        results = [0, 65, -65, 42, -42, 45.14, -38.86, 14.62, -651.12]
        ##
        # @brief Expected false results
        #
        false_results = [1, 3.85, 2.29, -1, 72, 45.141, -5, 26, 7]

        for equations in range(len(test_numbers)):
            self.assertEqual(math.addition(test_numbers[equations][0], test_numbers[equations][1]), results[equations])
            self.assertNotEqual(math.addition(test_numbers[equations][0], test_numbers[equations][1]), false_results[equations])

    ##
    # @brief Testing subtraction
    # Looping through pairs of testing numbers, passing them into given function
    # and comparing results with the expected ones.
    #
    def test_subtraction(self):
        test_numbers = [[0, 0], [42, 23], [-42, -23], [42, 0], [0, -42],
                        [3.14, 42], [-42, 3.14], [11.9, 2.72], [14.88, -666.0]]
        results = [0, 19, -19, 42, 42, -38.86, -45.14, 9.18, 680.88]
        false_results = [1, 3.85, 2.29, -1, 72, 45.141, -5, 26, 7]

        for equations in range(len(test_numbers)):
            self.assertEqual(math.subtraction(test_numbers[equations][0], test_numbers[equations][1]), results[equations])
            self.assertNotEqual(math.subtraction(test_numbers[equations][0], test_numbers[equations][1]), false_results[equations])

    ##
    # @brief Testing multiplication
    # Looping through pairs of testing numbers, passing them into given function
    # and comparing results with the expected ones.
    #
    def test_multiplication(self):
        test_numbers = [[0, 0], [42, 23], [-42, -23], [42, 0], [0, -42],
                        [3.14, 42], [-42, 3.14], [11.9, 2.72], [14.88, -666.0]]
        results = [0, 966, 966, 0, 0, 131.88, -131.88, 32.368, -9910.08]
        false_results = [3.85, 2.29, 1, -1, 666, 42, 3, 9, 0]

        for equations in range(len(test_numbers)):
            self.assertEqual(math.multiplication(test_numbers[equations][0], test_numbers[equations][1]), results[equations])
            self.assertNotEqual(math.multiplication(test_numbers[equations][0], test_numbers[equations][1]), false_results[equations])

    ##
    # @brief Testing division
    # Looping through pairs of testing numbers, passing them into given function
    # and comparing results with the expected ones.
    # Expected raising zero division error
    #
    def test_division(self):
        test_numbers = [[42, 21], [-42, -2], [42, 1], [0, -42],
                        [3.14, 3.14], [-42, 32], [13.09, 11.9], [60, 120]]
        results = [2, 21, 42, 0, 1, -1.3125, 1.1, 0.5]
        false_results = [3.85, 2.29, 1, 0.2, 0, -10, -1.1, 42]

        for equations in range(len(test_numbers)):
            self.assertEqual(math.division(test_numbers[equations][0], test_numbers[equations][1]), results[equations])
            self.assertNotEqual(math.division(test_numbers[equations][0], test_numbers[equations][1]), false_results[equations])

        with self.assertRaises(ZeroDivisionError):
            math.division(10, 0)

    ##
    # @brief Testing power
    # Looping through pairs of testing numbers, passing them into given function
    # and comparing results with the expected ones.
    # Expected raising value error when passed float into function
    #
    def test_power(self):
        test_numbers = [[1, 2], [-10, 3], [1.5, 2], [0, 10], [0, 0], [42, 0]]
        results = [1, -1000, 2.25, 0, 1, 1]
        false_results = [3.85, 2.29, 1, 42, -1, 0]

        for equations in range(len(test_numbers)):
            self.assertEqual(math.power(test_numbers[equations][0], test_numbers[equations][1]), results[equations])
            self.assertNotEqual(math.power(test_numbers[equations][0], test_numbers[equations][1]), false_results[equations])

        with self.assertRaises(ValueError):
            math.power(8, 10.58)

        with self.assertRaises(ValueError):
            math.power(8, -3.14)

    ##
    # @brief Testing factorial
    # Looping through pairs of testing numbers, passing them into given function
    # and comparing results with the expected ones.
    # Expected raising value error when passing negative or float number into function
    #
    def test_factorial(self):
        test_numbers = [0, 1, 2, 5, 11]
        results = [1, 1, 2, 120, 39916800]
        false_results = [0, -2, 3, -120, 1]

        for equations in range(len(test_numbers)):
            self.assertEqual(math.factorial(test_numbers[equations]), results[equations])
            self.assertNotEqual(math.factorial(test_numbers[equations]), false_results[equations])

        with self.assertRaises(ValueError):
            math.factorial(-1)

        with self.assertRaises(ValueError):
            math.factorial(9.11)

    ##
    # @brief Testing root
    # Looping through pairs of testing numbers, passing them into given function
    # and comparing results with the expected ones.
    # Expected raising value error when passing even number as first arg and negative number as the second
    # Expected raising zero division error when passing negative number as first arg and zero as the second
    #
    def test_root(self):
        test_numbers = [[1, 1], [2, 0], [2.5, 0], [2, 4], [2, 0.25], [3, -0.027]]
        results = [1, 0, 0, 2, 0.5, -0.3]
        false_results = [0, 1, -120, 1, 9.11, -9.11]

        for equations in range(len(test_numbers)):
            self.assertEqual(math.root(test_numbers[equations][0], test_numbers[equations][1]), results[equations])
            self.assertNotEqual(math.root(test_numbers[equations][0], test_numbers[equations][1]), false_results[equations])

        with self.assertRaises(ValueError):
            math.root(2, -2)

        with self.assertRaises(ValueError):
            math.root(4, -5)

        with self.assertRaises(ValueError):
            math.root(-2, -2)

        with self.assertRaises(ZeroDivisionError):
            math.root(-2, 0)

        with self.assertRaises(ZeroDivisionError):
            math.root(-3, 0)

        with self.assertRaises(ZeroDivisionError):
            math.root(0, 0)

    ##
    # @brief Testing modulo
    # Looping through pairs of testing numbers, passing them into given function
    # and comparing results with the expected ones
    # Expected raising zero division error when passing 0 as the divisor
    #
    def test_modulo(self):
        test_numbers = [[42, 21], [-42, -2], [42, 4], [0, -42],
                        [3.14, 3.14], [-42, 32], [13.5, 11.58], [60, 120]]
        results = [0, 0, 2, 0, 0, 22, 1.92, 60]
        false_results = [-1, 1, -3, -120, 1, 9.11, -9.11, 61]

        for equations in range(len(test_numbers)):
            self.assertEqual(math.modulo(test_numbers[equations][0], test_numbers[equations][1]), results[equations])
            self.assertNotEqual(math.modulo(test_numbers[equations][0], test_numbers[equations][1]), false_results[equations])

        with self.assertRaises(ZeroDivisionError):
            math.modulo(1, 0)
