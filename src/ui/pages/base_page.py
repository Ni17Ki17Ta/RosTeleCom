from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)
    
    def click_element(self, locator):
        with allure.step("Клик по элементу"):
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            return element
    
    def send_keys(self, locator, text):
        with allure.step(f"Ввод текста: {text}"):
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            return element
    
    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
    
    def is_element_visible(self, locator):
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False
    
    def hover_element(self, locator):
        with allure.step("Наведение курсора"):
            element = self.wait.until(EC.visibility_of_element_located(locator))
            self.actions.move_to_element(element).perform()
            return element
    
    def scroll_to_element(self, locator):
        with allure.step("Скролл до элемента"):
            element = self.wait.until(EC.visibility_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            return element
    
    def scroll_to_bottom(self):
        with allure.step("Скролл в самый низ"):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")