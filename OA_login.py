from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from common.denglu import login

class OA_login(unittest.TestCase):
    # 登录网页
    def setUp(self):
        self.web1 = webdriver.Firefox()
        self.web1.get('http://192.168.0.122:808/login.aspx')
        time.sleep(2)

        # 登录账号
        self.web1.find_element_by_id('cbx_Remember').click()
        self.web1.find_element_by_id("tbx_UserName").send_keys('adm')
        self.web1.find_element_by_id('tbx_Password').send_keys('adm')
        self.web1.find_element_by_id('ibtLogin').click()

        # 断言 登录是否成功
        time.sleep(2)
        a1 = self.web1.title
        print(a1)
        b1='[未注册试用版]网络办公自动化软件 [WebOA 19.12.7278.20211 5用户] [2019-12-31到期]'
        self.assertEqual(a1,b1,msg='失败：用户账号或密码错误！')
        time.sleep(2)

    # 验证新建事务-正常输入能否正常保存

    def test_case5(self):
        # 进入新建事务界面
        self.web1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[1]').click()
        time.sleep(2)
        # 进入frame
        self.web1.switch_to.frame(2)
        # 输入空
        self.web1.find_element_by_css_selector('#subject').send_keys('测试1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input').send_keys('1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('机票')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input').send_keys('1000')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[4]/input').send_keys('经济舱')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input').send_keys('1000')
        self.web1.find_element_by_xpath('//*[@id="url"]').send_keys('测试备注')
        # 日历
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[4]/input').send_keys('2020-06-03')
        # 保存
        self.web1.find_element_by_xpath('//*[@id="save"]').click()
        # 断言 为空可否保存
        a5=self.web1.switch_to.alert.text
        print('kkkkkk',a5)
        b5='成功：当前事务创建成功！'
        self.assertEqual(a5,b5,msg='请按要求填写信息')
        time.sleep(3)


    # # 验证新建事务-主题为空能否弹出提示
    def test_case6(self):
        # 进入新建事务界面
        self.web1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[1]').click()
        time.sleep(2)
        # 进入frame
        self.web1.switch_to.frame(2)
        # 输入空
        self.web1.find_element_by_css_selector('#subject').click()
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input').send_keys('1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('机票')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input').send_keys('1000')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[4]/input').send_keys('经济舱')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input').send_keys('1000')
        self.web1.find_element_by_xpath('//*[@id="url"]').send_keys('测试备注')
        # 日历
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[4]/input').send_keys('2020-06-03')
        # 保存
        self.web1.find_element_by_xpath('//*[@id="save"]').click()
        # 断言 为空可否保存
        a6=self.web1.find_element_by_xpath('/html/body/div/div').text
        b6='!'
        self.assertEqual(a6,b6,msg='请按要求填写信息')
    # 验证新建事务-单据附件为空能否弹出提示
    def test_case7(self):
        # 进入新建事务界面
        self.web1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[1]').click()
        time.sleep(2)
        # 进入frame
        self.web1.switch_to.frame(2)
        # 输入空
        self.web1.find_element_by_css_selector('#subject').send_keys('测试1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input').click()
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('机票')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input').send_keys('1000')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[4]/input').send_keys('经济舱')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input').send_keys('1000')
        self.web1.find_element_by_xpath('//*[@id="url"]').send_keys('测试备注')
        # 日历
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[4]/input').send_keys('2020-06-03')
        # 保存
        self.web1.find_element_by_xpath('//*[@id="save"]').click()
        # 断言 为空可否保存
        a7=self.web1.find_element_by_xpath('/html/body/div/div').text
        b7='!'
        self.assertEqual(a7,b7,msg='请按要求填写信息')
    # 验证新建事务-费用项目为空能否弹出提示
    def test_case8(self):
        # 进入新建事务界面
        self.web1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[1]').click()
        time.sleep(2)
        # 进入frame
        self.web1.switch_to.frame(2)
        # 输入空
        self.web1.find_element_by_css_selector('#subject').send_keys('测试1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input').send_keys('1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').click()
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input').send_keys('1000')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[4]/input').send_keys('经济舱')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input').send_keys('1000')
        self.web1.find_element_by_xpath('//*[@id="url"]').send_keys('测试备注')
        # 日历
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[4]/input').send_keys('2020-06-03')
        # 保存
        self.web1.find_element_by_xpath('//*[@id="save"]').click()
        # 断言 为空可否保存
        a8=self.web1.find_element_by_xpath('/html/body/div/div').text
        b8='!'
        self.assertEqual(a8,b8,msg='请按要求填写信息')

    # 验证新建事务-序号1-金额为空能否弹出提示
    def test_case9(self):
        # 进入新建事务界面
        self.web1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[1]').click()
        time.sleep(2)
        # 进入frame
        self.web1.switch_to.frame(2)
        # 输入空
        self.web1.find_element_by_css_selector('#subject').send_keys('测试1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input').send_keys('1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('机票')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input').click()
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[4]/input').send_keys('经济舱')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input').send_keys('1000')
        self.web1.find_element_by_xpath('//*[@id="url"]').send_keys('测试备注')
        # 日历
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[4]/input').send_keys('2020-06-03')
        # 保存
        self.web1.find_element_by_xpath('//*[@id="save"]').click()
        # 断言 为空可否保存
        a9=self.web1.find_element_by_xpath('/html/body/div/div').text
        b9='!'
        self.assertEqual(a9,b9,msg='请按要求填写信息')

    # 验证新建事务-合计金额为空能否弹出提示
    def test_case10(self):
        # 进入新建事务界面
        self.web1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[1]').click()
        time.sleep(2)
        # 进入frame
        self.web1.switch_to.frame(2)
        # 输入空
        self.web1.find_element_by_css_selector('#subject').send_keys('测试1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input').send_keys('1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('机票')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input').send_keys('1000')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[4]/input').send_keys('经济舱')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input').click()
        self.web1.find_element_by_xpath('//*[@id="url"]').send_keys('测试备注')
        # 日历
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[4]/input').send_keys('2020-06-03')
        # 保存
        self.web1.find_element_by_xpath('//*[@id="save"]').click()
        # 断言 为空可否保存
        a10=self.web1.find_element_by_xpath('/html/body/div/div').text
        b10='!'
        self.assertEqual(a10,b10,msg='请按要求填写信息')


    #     验证新建事务-报销申请单-日期时间输入 为空 能否弹出提示框
    def test_case16(self):
        # 进入新建事务界面
        self.web1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[1]').click()
        time.sleep(2)
        # 进入frame
        self.web1.switch_to.frame(2)
        # 输入空
        self.web1.find_element_by_css_selector('#subject').send_keys('测试1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input').send_keys('1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('机票')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input').send_keys(' ')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[4]/input').send_keys('经济舱')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input').send_keys('1000')
        self.web1.find_element_by_xpath('//*[@id="url"]').send_keys('测试备注')
        # 日历
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[4]/input').click()
        # 保存
        self.web1.find_element_by_xpath('//*[@id="save"]').click()
        # 断言 为空可否保存
        a16=self.web1.find_element_by_xpath('/html/body/div/div').text
        b16='!'
        self.assertEqual(a16,b16,msg='请按要求填写信息')


    #     验证新建事务-报销申请单-序号1-金额输入 测试（汉字）能否弹出提示
    def test_case11(self):
        # 进入新建事务界面
        self.web1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[1]').click()
        time.sleep(2)
        # 进入frame
        self.web1.switch_to.frame(2)
        # 输入空
        self.web1.find_element_by_css_selector('#subject').send_keys('测试1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input').send_keys('1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('机票')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input').send_keys('测试')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[4]/input').send_keys('经济舱')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input').send_keys('1000')
        self.web1.find_element_by_xpath('//*[@id="url"]').send_keys('测试备注')
        # 日历
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[4]/input').send_keys('2020-06-03')
        # 保存
        self.web1.find_element_by_xpath('//*[@id="save"]').click()
        # 断言 为空可否保存
        a11=self.web1.find_element_by_xpath('/html/body/div/div').text
        b11='!'
        self.assertEqual(a11,b11,msg='请按要求填写信息')

    #     验证新建事务-报销申请单-序号1-金额输入 abc 能否弹出提示
    def test_case12(self):
        # 进入新建事务界面
        self.web1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[1]').click()
        time.sleep(2)
        # 进入frame
        self.web1.switch_to.frame(2)
        # 输入空
        self.web1.find_element_by_css_selector('#subject').send_keys('测试1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input').send_keys('1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('机票')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input').send_keys('abc')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[4]/input').send_keys('经济舱')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input').send_keys('1000')
        self.web1.find_element_by_xpath('//*[@id="url"]').send_keys('测试备注')
        # 日历
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[4]/input').send_keys('2020-06-03')
        # 保存
        self.web1.find_element_by_xpath('//*[@id="save"]').click()
        # 断言 为空可否保存
        a12=self.web1.find_element_by_xpath('/html/body/div/div').text
        b12='!'
        self.assertEqual(a12,b12,msg='请按要求填写信息')

    #     验证新建事务-报销申请单-序号1-金额输入 !@# 能否弹出提示
    def test_case13(self):
        # 进入新建事务界面
        self.web1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[1]').click()
        time.sleep(2)
        # 进入frame
        self.web1.switch_to.frame(2)
        # 输入空
        self.web1.find_element_by_css_selector('#subject').send_keys('测试1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input').send_keys('1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('机票')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input').send_keys('!@#')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[4]/input').send_keys('经济舱')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input').send_keys('1000')
        self.web1.find_element_by_xpath('//*[@id="url"]').send_keys('测试备注')
        # 日历
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[4]/input').send_keys('2020-06-03')
        # 保存
        self.web1.find_element_by_xpath('//*[@id="save"]').click()
        # 断言 为空可否保存
        a13=self.web1.find_element_by_xpath('/html/body/div/div').text
        b13='!'
        self.assertEqual(a13,b13,msg='请按要求填写信息')

    #     验证新建事务-报销申请单-序号1-金额输入 '空格' 能否弹出提示
    def test_case14(self):
        # 进入新建事务界面
        self.web1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[1]').click()
        time.sleep(2)
        # 进入frame
        self.web1.switch_to.frame(2)
        # 输入空
        self.web1.find_element_by_css_selector('#subject').send_keys('测试1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input').send_keys('1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('机票')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input').send_keys(' ')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[4]/input').send_keys('经济舱')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input').send_keys('1000')
        self.web1.find_element_by_xpath('//*[@id="url"]').send_keys('测试备注')
        # 日历
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[4]/input').send_keys('2020-06-03')
        # 保存
        self.web1.find_element_by_xpath('//*[@id="save"]').click()
        # 断言 为空可否保存
        a14=self.web1.find_element_by_xpath('/html/body/div/div').text
        b14='!'
        self.assertEqual(a14,b14,msg='请按要求填写信息')

    #     验证新建事务-报销申请单-日期时间输入 abc 能否弹出提示
    def test_case15(self):
        # 进入新建事务界面
        self.web1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[1]').click()
        time.sleep(2)
        # 进入frame
        self.web1.switch_to.frame(2)
        # 输入空
        self.web1.find_element_by_css_selector('#subject').send_keys('测试1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input').send_keys('1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('机票')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input').send_keys('1000')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[4]/input').send_keys('经济舱')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input').send_keys('1000')
        self.web1.find_element_by_xpath('//*[@id="url"]').send_keys('测试备注')
        # 日历
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[4]/input').send_keys('abc')
        # 保存
        self.web1.find_element_by_xpath('//*[@id="save"]').click()
        # 断言 为空可否保存
        a15=self.web1.find_element_by_xpath('/html/body/div/div').text
        b15='!'
        self.assertEqual(a15,b15,msg='请按要求填写信息')

    #     验证新建事务-报销申请单-日期时间输入 测试 能否弹出提示
    def test_case16(self):
        # 进入新建事务界面
        self.web1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[1]').click()
        time.sleep(2)
        # 进入frame
        self.web1.switch_to.frame(2)
        # 输入空
        self.web1.find_element_by_css_selector('#subject').send_keys('测试1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input').send_keys('1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('机票')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input').send_keys(' ')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[4]/input').send_keys('经济舱')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input').send_keys('1000')
        self.web1.find_element_by_xpath('//*[@id="url"]').send_keys('测试备注')
        # 日历
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[4]/input').send_keys('测试')
        # 保存
        self.web1.find_element_by_xpath('//*[@id="save"]').click()
        # 断言 为空可否保存
        a16=self.web1.find_element_by_xpath('/html/body/div/div').text
        b16='!'
        self.assertEqual(a16,b16,msg='请按要求填写信息')

    #     验证新建事务-报销申请单-日期时间输入 ！@# 能否弹出提示
    def test_case17(self):
        # 进入新建事务界面
        self.web1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[1]').click()
        time.sleep(2)
        # 进入frame
        self.web1.switch_to.frame(2)
        # 输入空
        self.web1.find_element_by_css_selector('#subject').send_keys('测试1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input').send_keys('1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('机票')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input').send_keys('1000')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[4]/input').send_keys('经济舱')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input').send_keys('1000')
        self.web1.find_element_by_xpath('//*[@id="url"]').send_keys('测试备注')
        # 日历
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[4]/input').send_keys('！@#')
        # 保存
        self.web1.find_element_by_xpath('//*[@id="save"]').click()
        # 断言 为空可否保存
        a17=self.web1.find_element_by_xpath('/html/body/div/div').text
        b17='!'
        self.assertEqual(a17,b17,msg='请按要求填写信息')

        #     验证新建事务-报销申请单-日期时间输入 ！@# 能否弹出提示

    def test_case18(self):
        # 进入新建事务界面
        self.web1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[1]').click()
        time.sleep(2)
        # 进入frame
        self.web1.switch_to.frame(2)
        # 输入空
        self.web1.find_element_by_css_selector('#subject').send_keys('测试1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[6]/input').send_keys('1')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[2]/input').send_keys('机票')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[3]/input').send_keys('1000')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[2]/td[4]/input').send_keys('经济舱')
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[2]/tbody/tr[6]/td[3]/input').send_keys('1000')
        self.web1.find_element_by_xpath('//*[@id="url"]').send_keys('测试备注')
        # 日历
        self.web1.find_element_by_xpath('/html/body/form/ol/li/table[1]/tbody/tr[2]/td[4]/input').send_keys(' ')
        # 保存
        self.web1.find_element_by_xpath('//*[@id="save"]').click()
        # 断言 为空可否保存
        a18 = self.web1.find_element_by_xpath('/html/body/div/div').text
        b18 = '!'
        self.assertEqual(a18, b18, msg='请按要求填写信息')
    """

    # 错误
    pass
    # 新建事务-已建事务
    # 新建事务-已建事务
    # 进入已建事务界面
    # def test_case19(self):
    #     self.web1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[2]').click()

    # def test_case20(self):
    #     self.web1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[2]').click()
    #     self.web1.switch_to.frame(2)
    #     self.web1.find_element_by_xpath('//*[@id="Date1"]').send_keys('2020-06-01')
    #     self.web1.find_element_by_xpath('//*[@id="Date2"]').send_keys('2020-06-01')
    #     self.web1.find_element_by_xpath('//*[@id="btnSearch"]').click()
    #     time.sleep(10)
    # 验证待办事务 办理流程能否成功

    # 待办事务
    pass
    """
    def test_case21(self):
        self.web1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[3]').click()
        time.sleep(1)
        self.web1.switch_to.frame(2)
        self.web1.find_element_by_id('GridView1_ctl02_lbt_Operation').click()
        # 验证选择不同意单选框能否保存成功

        # self.web1.switch_to.default_content()
        # self.web1.switch_to.frame(3)
        # self.web1.find_element_by_xpath('/html/body/form/dl[3]/dt[2]/label[2]/input').click()
        # self.web1.find_element_by_xpath('//*[@id="opinion"]').send_keys('不同意')
        # 事务办理-待办事务-办理-保存
        # self.web1.find_element_by_xpath('//*[@id="save"]').click()
        # 断言
        # a=self.web1.switch_to.alert.text
        # print(a)
        # b='成功：当前事务办理成功！'
        # self.assertEqual(a,b,msg='退回成功')
        # self.web1.switch_to.alert.accept()

        # 验证选择同意单选框能否保存成功
        self.web1.switch_to.default_content()
        time.sleep(2)
        self.web1.switch_to.frame(3)
        self.web1.find_element_by_xpath('/html/body/form/dl[3]/dt[2]/label[1]/input').click()
        self.web1.find_element_by_xpath('//*[@id="opinion"]').send_keys('同意')
        # 选择办理人
        time.sleep(2)
        self.web1.find_element_by_xpath('//*[@id="selectClerk"]').click()
        time.sleep(2)
        self.web1.switch_to.frame(1)
        self.web1.find_element_by_xpath('//*[@id="TreeView1n2CheckBox"]').click()
        time.sleep(2)
        self.web1.find_element_by_xpath('//*[@id="btn_Ok"]').click()
        time.sleep(2)
        self.web1.switch_to.default_content()
        self.web1.switch_to.frame(3)
        # self.web1.switch_to.parent_frame()
        # 点击保存（反馈：类型错误：无法访问死对象）
        self.web1.find_element_by_xpath('//*[@id="save"]').click()
        a=self.web1.switch_to.alert.text
        b='成功：当前事务办理成功！'
        self.assertEqual(a,b,msg='保存成功')
        self.web1.switch_to.alert.accept()

    # 验证待办事务-办理-为空能否提示

    def test_22(self):
        self.web1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[3]').click()
        time.sleep(1)
        self.web1.switch_to.frame(2)
        time.sleep(3)
        self.web1.find_element_by_id('GridView1_ctl02_lbt_Operation').click()
        self.web1.switch_to.default_content()
        self.web1.switch_to.frame(3)
        self.web1.find_element_by_xpath('//*[@id="save"]').click()
        a22=self.web1.find_element_by_xpath('/html/body/div/div').text
        print(a22)
        b22='!'
        self.assertEqual(a22,b22,msg='此处为空，无提示')

    # 事务办理-已建事务
    # 事务办理-已建事务-验证已建事务-主题 -浏览能否使用
    def test_case23(self):
        time.sleep(2)
        self.web1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[2]').click()
        time.sleep(2)
        self.web1.switch_to.frame(2)
        self.web1.find_element_by_xpath('//*[@id="GridView1_ctl02_lbtSubject"]').click()
        self.web1.switch_to.default_content()
        time.sleep(3)
        # 断言 主题浏览成功打开
        self.web1.switch_to.frame('AffairView128_ifm')
        a23=self.web1.find_element_by_xpath("//*[@id='id']").text
        print(a23)
        b23='128'
        self.assertEqual(a23,b23,msg='失败：主题浏览打开失败')

    # 事务办理-已建事务-验证已建事务-状态 -审批情况能否使用
    def test_case24(self):
        time.sleep(2)
        self.web1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[2]').click()
        time.sleep(2)
        self.web1.switch_to.frame(2)
        self.web1.find_element_by_xpath('//*[@id="GridView1_ctl02_lbtTitle"]').click()
        self.web1.switch_to.default_content()
        time.sleep(3)
        # 断言 状态-审批成功打开
        self.web1.switch_to.frame('tab_OaAffairList_ifm')
        # self.web1.switch_to.frame('mask')
        a24=self.web1.find_element_by_xpath("/html/body/div[3]/div/div[2]/span/table[1]/tbody/tr[2]/td[2]").text
        print(a24)
        b24='费用报销单-2006011454-2006011551-2006011551'
        self.assertEqual(a24,b24,msg='失败：审批打开失败')

    # 事务办理-查阅事务
    def test_case25(self):
        self.web1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[5]').click()
        time.sleep(3)
        self.web1.switch_to.frame(2)
        self.web1.find_element_by_xpath('//*[@id="GridView1_ctl02_lbtSubject"]').click()
        self.web1.switch_to.default_content()
        time.sleep(3)
        # 断言 主题浏览成功打开
        self.web1.switch_to.frame('AffairView19_ifm')
        a25=self.web1.find_element_by_xpath("//*[@id='id']").text
        print(a25)
        b25='19'
        self.assertEqual(a25,b25,msg='失败：主题浏览打开失败')

    # 事务办理-查阅事务-验证查阅事务-状态 -审批情况能否使用
    def test_case26(self):
        time.sleep(2)
        # 点击查阅事务
        self.web1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[5]').click()
        time.sleep(2)
        # 点击第一行主题事务
        self.web1.switch_to.frame(2)
        self.web1.find_element_by_xpath('//*[@id="GridView1_ctl02_lbtTitle"]').click()
        self.web1.switch_to.default_content()
        time.sleep(3)
        # 断言 状态-审批成功打开
        self.web1.switch_to.frame('tab_OaAffairFind_ifm')
        a26=self.web1.find_element_by_xpath("/html/body/div[3]/div/div[2]/span/table[1]/tbody/tr[2]/td[2]").text
        print(a26)
        b26='费用报销单-2006011454'
        self.assertEqual(a26,b26,msg='失败：审批打开失败')

    # 事务办理-已建事务 验证删除事务能否使用
    def test_case27(self):
        time.sleep(2)
        self.web1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[2]').click()
        time.sleep(5)
        self.web1.switch_to.frame('tab_OaAffairList_ifm')
        self.web1.find_element_by_xpath('//*[@id="GridView1_ctl01_cbxCheckAll"]').click()
        time.sleep(2)
        self.web1.find_element_by_xpath('//*[@id="GridView1_ctl23_lbtDeleteAll"]').click()
        time.sleep(2)
        a27=self.web1.switch_to.alert.text
        time.sleep(2)

        print(a27)
        b27='您确定要批量删除选择的事务吗？'
        self.assertEqual(a27,b27,msg='删除失败')
        time.sleep(2)
        # self.web1.switch_to.alert.dismiss()
        self.web1.switch_to.alert.accept()

        # 事务办理-已建事务 验证批量删除事务能否使用
        def test_case28(self):
            time.sleep(2)
            self.web1.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/ul[3]/li[2]').click()
            time.sleep(5)
            self.web1.switch_to.frame('tab_OaAffairList_ifm')
            self.web1.find_element_by_xpath('//*[@id="GridView1_ctl01_cbxCheckAll"]').click()
            time.sleep(2)
            self.web1.find_element_by_xpath('//*[@id="GridView1_ctl23_lbtDeleteAll"]').click()
            time.sleep(2)
            a28 = self.web1.switch_to.alert.text
            time.sleep(2)

            print(a28)
            b28 = '您确定要批量删除选择的事务吗？'
            self.assertEqual(a28, b28, msg='删除失败')
            time.sleep(2)
            # self.web1.switch_to.alert.dismiss()
            self.web1.switch_to.alert.accept()
            time.sleep(3)

    
        time.sleep(3)

    def tearDown(self):
        time.sleep(3)
        self.web1.quit()


if __name__ == '__main__':
    unittest.main()
    # discover = unittest.TestSuite