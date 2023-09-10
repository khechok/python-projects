number = int(input('please enter a number: '))
if number % 2 == 0:
   print( str(number) + ' is even number!')
else:
   print( str(number) + ' is odd number')


import unittest

# Function to check if a number is even
def is_even(number):
    return number % 2 == 0

# Function to check if a number is odd
def is_odd(number):
    return number % 2 != 0

class TestOddEven(unittest.TestCase):

    def test_even_number(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))

    def test_odd_number(self):
        self.assertTrue(is_odd(3))
        self.assertFalse(is_odd(4))

if __name__ == '__main__':
    unittest.main()
print('test sucessfull!')