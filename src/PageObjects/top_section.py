from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located


class TopSection():
    WOMEN_MENU = (By.XPATH, '//div[@id="block_top_menu"]/ul/li/a[@title="Women"]')
    WOMEN_SUBMENU_PARENT = (By.XPATH, '//div[@id="block_top_menu"]/ul/li/a[@title="Women"]/following-sibling::ul')
    DRESSES_MENU = (By.XPATH, '//div[@id="block_top_menu"]/ul/li/a[@title="Dresses"]')
    TSHIRTS_MENU = (By.XPATH, '//div[@id="block_top_menu"]/ul/li/a[@title="T-Shirts"]')


    def __init__(self, driver):
        self.driver = driver

    def _check_attribute(self, element_to_check, value_to_check):
        is_att = value_to_check in element_to_check.get_attribute('style')
        return is_att

    def _hover_over(self, element):
        ac = ActionChains(self.driver)
        ac.move_to_element(element)
        ac.perform()

    def women_menu_hover(self):
        w_menu = self.driver.find_element(*self.WOMEN_MENU)
        self._hover_over(w_menu)
        WebDriverWait(self.driver, 2).until(visibility_of_element_located(self.WOMEN_SUBMENU_PARENT))
        w_submenu = self.driver.find_element(*self.WOMEN_SUBMENU_PARENT)
        is_hover = self._check_attribute(w_submenu, 'block')
        return is_hover

    def dresses_menu_hover(self):
        pass

    def tshirts_menu_hover(self):
        pass
