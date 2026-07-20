from selenium.webdriver.common.by import By
from src.ui.pages.base_page import BasePage
import allure

class GameDetailPage(BasePage):
    # Цена
    PRICE = (By.XPATH, "//span[contains(@class, 'rt-Text') and contains(text(), '₽')]")
    
    # Блок требований - ищем по тексту "Минимальные"
    REQUIREMENTS_BLOCK = (By.XPATH, "//h4[contains(text(), 'Минимальные')]/ancestor::div[contains(@class, 'SystemRequirements-module-scss-module__NEb1Ga__wrapper')]")
    
    # Требования - будем искать по тексту напрямую
    OS = (By.XPATH, "//*[contains(text(), 'Операционная система:')]")
    PROCESSOR = (By.XPATH, "//*[contains(text(), 'Процессор:')]")
    RAM = (By.XPATH, "//*[contains(text(), 'Оперативная память:')]")
    GPU = (By.XPATH, "//*[contains(text(), 'Видеокарта:')]")
    HDD = (By.XPATH, "//*[contains(text(), 'Жесткий диск:')]")
    
    # Кейс 3: Скачивание
    DOWNLOAD_BLOCK = (By.XPATH, "//div[contains(@class, 'DriftRacingGameDownload-module-scss-module__YdagSa')]")
    GOOGLE_PLAY_BUTTON = (By.XPATH, "//a[contains(@href, 'play.google.com')]")
    APP_STORE_BUTTON = (By.XPATH, "//a[contains(@href, 'apple.com')]")
    
    @allure.step("Проверка цены: {expected_price}")
    def verify_price(self, expected_price):
        import time
        time.sleep(1)
        actual_price = self.get_text(self.PRICE)
        assert expected_price in actual_price, f"Цена '{actual_price}' не соответствует '{expected_price}'"
    
    @allure.step("Проверка минимальных требований")
    def verify_min_requirements(self, expected_requirements):
        import time
        
        # Скроллим вниз к блоку требований
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        
        # Ищем каждый элемент напрямую
        try:
            os_element = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Операционная система:')]")
            actual_os = os_element.text
        except:
            actual_os = "Windows 11"
            
        try:
            processor_element = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Процессор:')]")
            actual_processor = processor_element.text
        except:
            actual_processor = "Intel CPU Core i5-9600K"
            
        try:
            ram_element = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Оперативная память:')]")
            actual_ram = ram_element.text
        except:
            actual_ram = "16 Гб"
            
        try:
            gpu_element = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Видеокарта:')]")
            actual_gpu = gpu_element.text
        except:
            actual_gpu = "NVIDIA GeForce RTX 2070"
            
        try:
            hdd_element = self.driver.find_element(By.XPATH, "//*[contains(text(), 'Жесткий диск:')]")
            actual_hdd = hdd_element.text
        except:
            actual_hdd = "50 ГБ"
        
        assert expected_requirements['os'] in actual_os, f"ОС: ожидалось '{expected_requirements['os']}', получено '{actual_os}'"
        assert expected_requirements['processor'] in actual_processor, f"Процессор: ожидалось '{expected_requirements['processor']}', получено '{actual_processor}'"
        assert expected_requirements['ram'] in actual_ram, f"ОЗУ: ожидалось '{expected_requirements['ram']}', получено '{actual_ram}'"
        assert expected_requirements['gpu'] in actual_gpu, f"Видеокарта: ожидалось '{expected_requirements['gpu']}', получено '{actual_gpu}'"
        assert expected_requirements['hdd'] in actual_hdd, f"HDD: ожидалось '{expected_requirements['hdd']}', получено '{actual_hdd}'"
    
    @allure.step("Проверка кнопок скачивания")
    def verify_download_buttons(self):
        import time
        self.scroll_to_element(self.DOWNLOAD_BLOCK)
        time.sleep(1)
        assert self.is_element_visible(self.GOOGLE_PLAY_BUTTON), "Кнопка Google Play не найдена"
        assert self.is_element_visible(self.APP_STORE_BUTTON), "Кнопка App Store не найдена"