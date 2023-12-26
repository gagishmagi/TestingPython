from unittest import TestCase, TestSuite
import unittest

from Calculator.main import add, substract, multi, devide


#
# class Test(TestCase):
#
#     def test_add1(self):
#         self.assertEquals(add(2, 3), 8)
#
#     def test_add2(self):
#         self.assertGreaterEqual(add(5, 7), 12)
#
#     def test_add3(self):
#         self.assertEquals(add(10, -4), 6)
#
#     def test_add4(self):
#         self.assertEquals(add(0, -4), -4)
#
#     def test_substract(self):
#         self.assertLess(substract(6, 4), 3)
#
#     def test_multi(self):
#         self.fail()
#
#     def test_devide(self):
#         self.fail()

class simpleTest2(TestCase):
    def setUp(self):
        self.a = 10
        self.b = 20
        name = self.shortDescription()
        print("The", name, "of", self.a, "and", self.b)
        if name == "Add":
            self.a = 0
            self.b = 100
            print("The", name, "of", self.a, "and", self.b)
        if name == "Sub":
            self.a = 50
            self.b = 60
            print("The", name, "of", self.a, "and", self.b)

    def tearDown(self):
        print("\nend of test", self.shortDescription())

    def testAdd(self):
        '''Add'''
        result = add(self.a, self.b)
        self.assertTrue(result == 100)

    def testsub(self):
        '''Sub'''
        result = substract(self.a, self.b)
        self.assertTrue(result == -10)

    def testMulti(self):
        '''Mult'''
        result = multi(self.a, self.b)
        self.assertTrue(result == 200)

    def testDevideByZero(self):
        with self.assertRaises(ZeroDivisionError):
            devide(5,0)

#
#
# if __name__ == '__main__':
#     unittest.main()
#
#
# class simpleTest3(TestCase):
#     def setUp(self):
#         self.a = 10
#         self.b = 20
#
#     def testadd(self):
#         """Add"""
#         result = self.a + self.b
#         self.assertTrue(result == 100)
#
#     def testsub(self):
#         """sub"""
#         result = self.a - self.b
#         self.assertTrue(result == -10)
#
#
# def suite():
#     suite = TestSuite()
#     # suite.addTest(simpleTest3)
#     suite.addTest(simpleTest2)
#     return suite
#
#
# if __name__ == '__main__':
#     runner = unittest.TextTestRunner()
#     test_suite = suite()
#     result = runner.run(test_suite)
#
#
#     print("--- START OF TEST RESULTS ----")
#     print(result)
#
#     print("result::failures")
#     print(result.failures)
#
#     print("result::skipped")
#     print(result.skipped)
