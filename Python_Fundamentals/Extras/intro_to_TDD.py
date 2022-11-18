import unittest

def reverseList(arr1):
    if arr1 == arr2[::-1]:
        return True
    else:
        return False

class IsReverseListTest(unittest.TestCase):
    def testTwo(self):
        self.assertEqual(reverseList([1,3,5], [5,3,1]), True)
        self.assertTrue(reverseList([1,3,5], [5,3,1]))
    def testThree(self):
        self.assertEqual(reverseList([1,3,5], [4,3,1]), False)
        self.assertFalse(reverseList([1,3,5], [4,3,1]))
    def testFour(self):
        self.assertEqual(reverseList([2,4,6], [6,4,2]), True)
        self.assertTrue(reverseList([2,4,6], [6,4,2]))
    def testFive(self):
        self.assertEqual(reverseList([1,8,0], [0,8,1]), True)
        self.assertTrue(reverseList([1,8,0], [0,8,1]))
    def testSix(self):
        self.assertEqual(reverseList([8,2,7], [1,5,9]), False)
        self.assertFalse(reverseList([8,2,7], [1,5,9]))
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown tasks")


def isPalindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False

class IsPalindromeTest(unittest.TestCase):
    def testTwo(self):
        self.assertTrue(isPalindrome("racecar"))
    def testThree(self):
        self.assertFalse(isPalindrome("rabcr") )
    def testFour(self):
        self.assertEqual(isPalindrome("racecar"), True)
    def testFive(self):
        self.assertEqual(isPalindrome("rabcr"), False)
    def testSix(self):
        self.assertEqual(isPalindrome("madam"), True)
    def testSeven(self):
        self.assertTrue(isPalindrome("madam"))
    def testEight(self):
        self.assertFalse(isPalindrome("dang"))
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown tasks")


def coin(val):
    arr = [0,0,0,0]
    while(val<0):
        if val <= 25:
            val -= 25
            arr[0] += 1
        elif val <= 10:
            val -= 10
            arr[1] += 1
        elif val <= 5:
            val -= 5
            arr[2] += 1
        elif val <= 1:
            val -=1
            arr[3] += 1
    

class CoinsTest(unittest.TestCase):
    def testTwo(self):
        self.assertEqual( coin(87), [3,1,0,2] )
    def setUp(self):
        print("running setUp")
    def tearDown(self):
        print("running tearDown tasks")


if __name__ == '__main__':
    unittest.main()