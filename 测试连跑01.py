from selenium import webdriver
web1=webdriver.Firefox()
import unittest
import  time

class Tceshi(unittest.TestCase):
    def setUp(self):
        print(000)

    def test_casel(self):
        print(111)

    def test_case2(self):
        print(222)

    def test_case3(self):
        print(333)

    def test_case4(self):
        print(444)

    def test_case5(self):
        print(666)

    def tearDown(self):
        time.sleep(2)

        self.web1.close()
        self.web1.quit()

if __name__ == '__main__':
    unittest.main()
