from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
class Baidul_lianpao(unittest.TestCase):
    def setUp(self):
        self.web1 = webdriver.Firefox()
    def test_01(self):
        self.web1.get('http://www.baidu.com')
        time.sleep(3)
        self.web1.find_element_by_id('kw').send_keys('迪丽热巴')
        self.web1.find_element_by_id('su').click()

    def test_02(self):

        self.web1.get('https://passport.meituan.com/account/unitivelogin')
        time.sleep(3)
        self.web1.find_element_by_link_text('免费注册').click()
        time.sleep(7)

    def test_03(self):

        self.web1.get('https://passport.meituan.com/account/unitivelogin?')
        time.sleep(3)
        self.web1.find_element_by_css_selector('.signup-guide > a:nth-child(1)').click()
        time.sleep(7)

    def test_04(self):

        self.web1.get('https://www.baidu.com')
        time.sleep(3)
        self.web1.find_element_by_id('kw').send_keys('迪丽热巴')
        time.sleep(10)
        self.web1.find_element_by_css_selector("[value='百度一下']").submit()
        time.sleep(7)


    def test_06(self):

        self.web1.get("https://www.baidu.com")
        a = self.web1.current_url
        print(a)

    def test_07(self):

        self.web1.get("https://www.baidu.com")
        a=self.web1.find_element_by_id("kw").get_attribute("name")
        print(a)

    def test_08(self):

        a=self.web1.name
        print(a)

    def test_09(self):

        self.web1.get("https://www.baidu.com")
        time.sleep(3)
        ActionChains(self.web1).move_to_element(self.web1.find_element_by_id("s-usersetting-top")).perform()
        time.sleep(2)
        self.web1.find_element_by_class_name('setpref').click()

    def tearDown(self):
        time.sleep(3)
        self.web1.close()
        self.web1.quit()
if __name__ == '__main__':
    unittest.main()