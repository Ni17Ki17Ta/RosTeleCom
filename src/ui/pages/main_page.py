from selenium.webdriver.common.by import By
from src.ui.pages.base_page import BasePage
import allure
from selenium.webdriver.common.action_chains import ActionChains

class MainPage(BasePage):
    GAMES_MENU = (By.XPATH, "//a[contains(text(), 'Игры')]")
    PC_SUBMENU = (By.XPATH, "//a[contains(text(), 'PC')]")
    
    @allure.step("Наведение на меню Игры и выбор PC")
    def hover_games_and_select_pc(self):
        import time
        
        # Находим меню "Игры"
        games_menu = self.driver.find_element(*self.GAMES_MENU)
        
        # Создаем цепочку действий
        actions = ActionChains(self.driver)
        actions.move_to_element(games_menu).perform()
        
        # Ждем появления подменю
        time.sleep(1)
        
        # Ищем "PC" и кликаем
        try:
            pc_submenu = self.driver.find_element(*self.PC_SUBMENU)
            pc_submenu.click()
        except:
            # Если не нашли "PC", ищем через XPath
            pc_submenu = self.driver.find_element(By.XPATH, "//a[contains(@href, 'pc')]")
            pc_submenu.click()
        
        time.sleep(1)