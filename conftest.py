import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import allure
import os

@pytest.fixture(scope="function")
def driver():
    """Фикстура с локальным ChromeDriver"""
    
    # ПУТЬ К ВАШЕМУ ЛОКАЛЬНОМУ ДРАЙВЕРУ!
    driver_path = os.path.join(os.path.dirname(__file__), "drivers", "chrome", "chromedriver.exe")
    
    # Проверяем, что драйвер существует
    if not os.path.exists(driver_path):
        raise Exception(f"❌ Драйвер не найден: {driver_path}")
    
    print(f"✅ Использую драйвер: {driver_path}")
    
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    
    print("🚀 Запускаю Chrome...")
    
    driver = webdriver.Chrome(
        service=Service(driver_path),
        options=chrome_options
    )
    
    driver.implicitly_wait(10)
    
    yield driver
    
    print("🔚 Закрываю Chrome...")
    driver.quit()

@pytest.fixture(scope="session")
def api_base_url():
    return "http://185.193.143.49:8080"

@pytest.fixture(scope="session")
def ui_base_url():
    return "https://igrovoy.rt.ru/"