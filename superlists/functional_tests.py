from selenium import webdriver
import unittest
import time
class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()
        #self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        #网站标题和头部都包含"To-Do"这个词
        self.assertIn('To-Do',self.browser.title)

        self.fail("Finish the test")
        #应用邀请她输入一个待办事项

        #她在一个文本框中输入了"Buy peacock feathers"（购买孔雀羽毛）
        #伊利丝的爱好是使用假蝇做饵钓鱼

        #她按回车键后页面更新了
        #待办事项表格中显示了"1. Buy  peacock featers"

        #页面中有显示了一个文本框，可以输入其他的待办事项
        #她输入了"Use peacock feathers to make a fly"
        #伊利丝做事很有条理

        #页面再次更新，显示这两个代办事项

        #伊利斯想知道这个网站是否会记住她的清单

        #她看到网站为她声称了一个唯一的URL

        #而且页面中有一些文字解说这个功能

        #访问URL，发现待办事项都在

        #她很满意，去睡觉了

if __name__=='__main__':
    unittest.main()
