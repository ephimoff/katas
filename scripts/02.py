# Karate Chop
import unittest

print("Hello from Kata 02")

def chop( x, array ):
  return

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