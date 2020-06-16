from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from HTMLTestRunnerNew import HTMLTestRunner
# test_dir='./'
# discovery=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

class Tceshi(unittest.TestCase):
    def setUp(self):
        self.web1=webdriver.Firefox()
        self.web1.get('https://mail.qq.com/')
        time.sleep(3)

    def test_casel(self):
        time.sleep(3)
        self.web1.switch_to.frame('login_frame')
        self.web1.find_element_by_id('u').send_keys('3060827971')
        self.web1.find_element_by_id('p').send_keys('ldoudou1')
        self.web1.find_element_by_css_selector('#login_button').click()

        time.sleep(5)
        a1=self.web1.title
        print(a1)
        b1='QQ邮箱'
        self.assertEqual(a1,b1,msg='你还没有输入帐号！！！')
        time.sleep(2)


    # def test_case2(self):
    #     print("aaaaaaaaaaa")
    #     time.sleep(3)
    #     self.web1.switch_to.frame('login_frame')
    #
    #
    #     self.web1.find_element_by_id('u').click()
    #     self.web1.find_element_by_css_selector('#p').send_keys('ldoudou1')
    #     self.web1.find_element_by_css_selector('#login_button').click()
    #     a2 = self.web1.find_element_by_css_selector('#err_m').text
    #     b2= '你还没有输入帐号！'
    #     self.assertEqual(a2,b2, msg='你还没有输入帐号！！！')
    #
    # def test_case3(self):
    #     print("aaaaaaaaaaa")
    #     time.sleep(3)
    #     self.web1.switch_to.frame('login_frame')
    #
    #     self.web1.find_element_by_css_selector('#u').clear()
    #     self.web1.find_element_by_css_selector('#u').send_keys('3060827971')
    #     self.web1.find_element_by_css_selector('#p').click()
    #     self.web1.find_element_by_css_selector('#login_button').click()
    #     a3= self.web1.find_element_by_css_selector('#err_m').text
    #     b3= '你还没有输入密码！'
    #     self.assertEqual(a3,b3, msg='你还没有输入密码！！！')
    #
    # def test_case4(self):
    #     print("aaaaaaaaaaa")
    #     time.sleep(3)
    #     self.web1.switch_to.frame('login_frame')
    #
    #     self.web1.find_element_by_css_selector('#u').clear()
    #     self.web1.find_element_by_css_selector('#u').send_keys('四五四四五六八九二')
    #     self.web1.find_element_by_css_selector('#p').send_keys('ldoudou1')
    #     self.web1.find_element_by_css_selector('#login_button').click()
    #     a4= self.web1.find_element_by_css_selector('#err_m').text
    #     b4= '请输入正确的帐号！'
    #     self.assertEqual(a4,b4, msg='请输入正确的帐号！！！')
    #
    # def test_case5(self):
    #     print("aaaaaaaaaaa")
    #     time.sleep(3)
    #     self.web1.switch_to.frame('login_frame')
    #     self.web1.find_element_by_css_selector('#u').clear()
    #     self.web1.find_element_by_css_selector('#u').send_keys('454456892')
    #     self.web1.find_element_by_css_selector('#p').send_keys('ldoudou1')
    #     self.web1.find_element_by_css_selector('#login_button').click()
    #     a5= self.web1.find_element_by_css_selector('#err_m').text
    #     b5= '你输入的帐号或密码不正确，请重新输入。'
    #     self.assertEqual(a5,b5, msg='你输入的帐号或密码不正确，请重新输入。！！')



    def tearDown(self):
        time.sleep(2)

        self.web1.close()
        self.web1.quit()

if __name__ == '__main__':
    # unittest.main()
    d=unittest.TestSuite()
    d.addTest(Tceshi('test_casel'))
    # d.addTest(Tceshi('test_case2'))
    # d.addTest(Tceshi('test_case3'))
    # d.addTest(Tceshi('test_case4'))
    # d.addTest(Tceshi('test_case5'))
    report_dir='./Test_Report/'
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    report_name=report_dir+now+'result.html'
    with open(report_name,'wb')as f:
        runner=HTMLTestRunner(stream=f,title='Test Report',description='Test Case Result')
        runner.run(d)
