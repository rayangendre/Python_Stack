import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
#from stack_array import Stack
from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)
    
    def test_simple_2(self):
        #checks that the pop and isEmpty method are working
        stack = Stack(7)
        stack.push(3)
        self.assertFalse(stack.is_empty())
        stack.pop()
        self.assertTrue(stack.is_empty())

    def test_simple_3(self):
        #checks the is_full method for working
        stack = Stack(1)
        stack.push(4)
        self.assertTrue(stack.is_full)
        

    def test_simple_4(self):
        #checks the peek method
        stack = Stack(0)
        with self.assertRaises(IndexError):
            stack.peek()

        stack = Stack(7)
        stack.push(4)
        stack.push(3)
        self.assertEqual(stack.peek(), 3)
        stack.pop()
        self.assertEqual(stack.peek(), 4)
    
    def test_simple_5(self):
        #testing of the push method
        stack = Stack(2)
        stack.push(3)
        stack.push(2)
        with self.assertRaises(IndexError):
            stack.push(4)

    def test_simple_6(self):
        #testing of the pop method
        stack = Stack(0)
        with self.assertRaises(IndexError):
            stack.pop()
    
    def test_simple_7(self):
        #testing of none
        stack = Stack(None)
        with self.assertRaises(IndexError):
            stack.push('hello')
    
    def test_simple_8(self):
        stack = Stack(0)
        self.assertTrue(stack.is_full)
    

        


if __name__ == '__main__': 
    unittest.main()
