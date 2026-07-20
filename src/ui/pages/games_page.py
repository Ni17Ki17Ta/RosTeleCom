from selenium.webdriver.common.by import By
from src.ui.pages.base_page import BasePage
import allure

class GamesPage(BasePage):
    # Поиск
    SEARCH_INPUT = (By.XPATH, "//input[@placeholder='Поиск']")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(@class, 'HeaderSearchBar-module-scss-module__jAlznG__button')]")
    
    # Карточка игры
    GAME_CARD = (By.XPATH, "//div[.//span[contains(text(), '₽')]]")
    GAME_TITLE = (By.XPATH, ".//a[contains(@class, 'ProductCard-module-scss-module__Dsx4oa__title')]")
    GAME_PRICE = (By.XPATH, ".//span[contains(text(), '₽')]")
    
    @allure.step("Поиск игры: {game_name}")
    def search_game(self, game_name):
        import time
        from selenium.webdriver.common.keys import Keys
        self.send_keys(self.SEARCH_INPUT, game_name)
        time.sleep(0.5)
        try:
            self.click_element(self.SEARCH_BUTTON)
        except:
            search_input = self.driver.find_element(*self.SEARCH_INPUT)
            search_input.send_keys(Keys.RETURN)
        time.sleep(2)
    
    @allure.step("Открытие карточки игры с ценой {expected_price}")
    def open_first_game_card_with_price(self, expected_price):
        import time
        time.sleep(3)
        cards = self.driver.find_elements(*self.GAME_CARD)
        print(f"Найдено карточек: {len(cards)}")
        for card in cards:
            try:
                price_element = card.find_element(*self.GAME_PRICE)
                price = price_element.text
                print(f"Цена: {price}")
                if expected_price in price:
                    try:
                        title_link = card.find_element(By.XPATH, ".//a[contains(@class, 'ProductCard-module-scss-module__Dsx4oa__title')]")
                        title_link.click()
                        return True
                    except:
                        try:
                            details_btn = card.find_element(By.XPATH, ".//button[contains(@class, 'product-card-details')]")
                            details_btn.click()
                            return True
                        except:
                            card.click()
                            return True
            except Exception as e:
                print(f"Ошибка: {e}")
                continue
        return False
    
    @allure.step("Поиск игры {game_name} в списке")
    def find_game_in_list(self, game_name):
        import time
        time.sleep(3)
        titles = self.driver.find_elements(By.XPATH, "//a[contains(@class, 'ProductCard-module-scss-module__Dsx4oa__title')]")
        print(f"Найдено названий: {len(titles)}")
        for title in titles:
            try:
                title_text = title.text
                print(f"Название: {title_text}")
                if game_name.lower() in title_text.lower():
                    title.click()
                    return True
            except:
                continue
        return False
    
    @allure.step("Переход на страницу {page_number}")
    def go_to_page(self, page_number):
        import time
        page_btn = self.driver.find_element(By.XPATH, f"//span[contains(@class, 'Pagination-module-scss-module__7rqbBa__pageItem') and text()='{page_number}']")
        page_btn.click()
        time.sleep(2)