import unittest
from main import *

class TestStringMethods(unittest.TestCase):
# ========================================================================
    def testAddTwo(self):
        a = add("1,2")
        self.assertEqual(a, 3, "ERROR: Dodawanie '1,2'")
    def testAddOne(self):
        c= add("1")
        self.assertEqual(c,1,"ERROR: Dodawanie '1'")
    def testAddEmpty(self):
        b = add("")
        self.assertEqual(b,0,"ERROR: Dodawanie ''")
    def testAddJustAComa(self):
        b = add(",")
        self.assertEqual(b,0,"ERROR: Dodawanie ','")

#========================================================================
    def  testAddMultylyNumber(self):
        a = add("1,1,1")
        self.assertEqual(a,3,"ERROR: Dodawanie '1,1,1'")
#========================================================================
    def testAddWhiteSpace(self):
        a = add("1\n2,3")
        self.assertEqual(a,6, "ERROR: Dodawanie '1,\\n2,\\t3'")
    def testAddWith(self):
        with self.assertRaises(ValueError):
            a = add("1,\n2")
