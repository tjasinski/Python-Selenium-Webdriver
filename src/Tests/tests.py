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

    def test_home_page_menu(self):
        top = TopSection(self.driver)
        women = top.women_menu_hover()
        self.assertTrue(women, '<Women> submenu is not displayed')
        dresses = top.dresses_menu_hover()
        self.assertTrue(dresses, '<Dresses> submenu is not displayed')



if __name__ == '__main__':
    unittest.main()