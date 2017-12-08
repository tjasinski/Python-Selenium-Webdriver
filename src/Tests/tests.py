import unittest

from src.PageObjects.top_section import TopSection
from src.TestData.data import TestData
from selenium import webdriver


class MainPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(1)
        self.driver.maximize_window()
        self.driver.get(TestData.URL)

    def tearDown(self):
        self.driver.quit()

    def test_loading_page(self):
        top = TopSection(self.driver)
        s = top.women_menu_hover()
        self.assertTrue(s)


if __name__ == '__main__':
    unittest.main()