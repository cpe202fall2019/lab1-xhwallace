import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_empty(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_max_list_various(self):
        tlist = [1, 2, 8, 7,]
        self.assertEqual(max_list_iter(tlist), 8)
        tlist = [1, 2, 7, 8, ]
        self.assertEqual(max_list_iter(tlist), 8)
        tlist = [2, 8, 1, 7, ]
        self.assertEqual(max_list_iter(tlist), 8)
        tlist = [8, 2, 1, 7, ]
        self.assertEqual(max_list_iter(tlist), 8)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1, 2, 3, 8, 2]), [2, 8, 3, 2, 1])

    def test_reverse_rec_empty(self):
        self.assertEqual(reverse_rec([]), [])

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )

        list_val = [0, 3, 4, 8, 10, 11, 15, 16, 17, 20]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(8, 0, len(list_val) - 1, list_val), 3)
        list_val = [0, 3, 4, 8, 10, 11, 15, 16, 17, 20]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(20, 0, len(list_val) - 1, list_val), 9)
if __name__ == "__main__":
        unittest.main()

    
