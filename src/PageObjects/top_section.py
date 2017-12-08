from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located


class TopSection():
    WOMEN_MENU = (By.XPATH, '//div[@id="block_top_menu"]/ul/li/a[@title="Women"]')
    WOMEN_SUBMENU_PARENT = (By.XPATH, '//div[@id="block_top_menu"]/ul/li/a[@title="Women"]/following-sibling::ul')
    DRESSES_MENU = (By.XPATH, '//div[@id="block_top_menu"]/ul/li/a[@title="Dresses"]')
    DRESSES_SUBMENU_PARENT = (By.XPATH, '//div[@id="block_top_menu"]/ul/li/a[@title="Dresses"]/following-sibling::ul')
    TSHIRTS_MENU = (By.XPATH, '//div[@id="block_top_menu"]/ul/li/a[@title="T-shirts"]')


    def __init__(self, driver):
        self.driver = driver

    def _check_style_attribute(self, element_to_check, value_to_check):
        is_att = value_to_check in element_to_check.get_attribute('style')
        return is_att

    def _hover_over(self, element_to_hover, submenu_to_be_visible):
        w_menu = self.driver.find_element(*element_to_hover)
        ac = ActionChains(self.driver)
        ac.move_to_element(w_menu)
        ac.perform()
        WebDriverWait(self.driver, 2).until(visibility_of_element_located(submenu_to_be_visible))
        w_submenu = self.driver.find_element(*submenu_to_be_visible)
        is_hover = self._check_style_attribute(w_submenu, 'block')
        return is_hover


    def women_menu_hover(self):
        return self._hover_over(self.WOMEN_MENU, self.WOMEN_SUBMENU_PARENT)

    def dresses_menu_hover(self):
        return self._hover_over(self.DRESSES_MENU, self.DRESSES_SUBMENU_PARENT)

