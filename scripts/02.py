# Karate Chop
import unittest

print("Kata 02 results:")

# Write a binary chop method that takes an integer search target and 
# a sorted array of integers. It should return the integer index of 
# the target in the array, or -1 if the target is not in the array. 
# ---
# Assumptions:
# The array has less than 100,000 elements. 
# Time and memory performance are not issues 

# iterative approach:
# def chop( x, array ):
#   # print("Looking for %s in this array: %s" % (x, array))
#   res = -1
#   if len(array) > 0:
#     for index in range(len(array)):
#       # print("Current index is %s and the value is %s" % (index, array[index]))
#       if array[index] == x:
#         res = index
#   return res

# Logarithmic approach:

# split array in half
def split_list(array):
  half = len(array)//2
  # print("Array: %s . Split as left: %s and right: %s" % (array, array[:half], array[half:]))
  return array[:half], array[half:]
  # return

# split_list([1, 3, 5])
# split_list([1])
# split_list([])
# split_list([1, 3, 5, 7])

def chop( x, array ):
  res = -1
  if len(array) > 0:
    left, right = split_list(array)
    if left[0] == x:
      res = 0

  return res




# Unit testing
class ChopTestCase(unittest.TestCase):
  # tests
  def test_chop(self):
    self.assertEqual(-1, chop(3, []))
    self.assertEqual(-1, chop(3, [1]))
    self.assertEqual(0,  chop(1, [1]))
    #
    self.assertEqual(0,  chop(1, [1, 3, 5]))
    self.assertEqual(1,  chop(3, [1, 3, 5]))
    self.assertEqual(2,  chop(5, [1, 3, 5]))
    self.assertEqual(-1, chop(0, [1, 3, 5]))
    self.assertEqual(-1, chop(2, [1, 3, 5]))
    self.assertEqual(-1, chop(4, [1, 3, 5]))
    self.assertEqual(-1, chop(6, [1, 3, 5]))
    #
    self.assertEqual(0,  chop(1, [1, 3, 5, 7]))
    self.assertEqual(1,  chop(3, [1, 3, 5, 7]))
    self.assertEqual(2,  chop(5, [1, 3, 5, 7]))
    self.assertEqual(3,  chop(7, [1, 3, 5, 7]))
    self.assertEqual(-1, chop(0, [1, 3, 5, 7]))
    self.assertEqual(-1, chop(2, [1, 3, 5, 7]))
    self.assertEqual(-1, chop(4, [1, 3, 5, 7]))
    self.assertEqual(-1, chop(6, [1, 3, 5, 7]))
    self.assertEqual(-1, chop(8, [1, 3, 5, 7]))

if __name__ == '__main__':
  unittest.main()