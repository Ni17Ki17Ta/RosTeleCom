import pytest
import allure
from src.ui.pages.main_page import MainPage
from src.ui.pages.games_page import GamesPage
from src.ui.pages.game_detail_page import GameDetailPage
from selenium.webdriver.common.by import By

@allure.epic("UI Тестирование игрового портала")
@allure.feature("Поиск и проверка игр")
class TestGames:
    
    @allure.story("Кейс 1: Поиск игры Pioner")
    @allure.title("Проверка поиска и цены игры Pioner")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    def test_search_pioner_game(self, driver, ui_base_url):
        with allure.step("Открытие главной страницы"):
            driver.get(ui_base_url)
        
        with allure.step("Наведение на меню Игры и выбор PC"):
            main_page = MainPage(driver)
            main_page.hover_games_and_select_pc()
        
        with allure.step("Поиск игры Pioner"):
            games_page = GamesPage(driver)
            games_page.search_game("Pioner")
        
        with allure.step("Открытие карточки игры с ценой 699₽"):
            result = games_page.open_first_game_card_with_price("699")
            assert result, "Игра с ценой 699₽ не найдена"
        
        with allure.step("Проверка цены в карточке"):
            game_detail = GameDetailPage(driver)
            game_detail.verify_price("699")
    
    @allure.story("Кейс 2: Проверка требований LEGO Batman")
    @allure.title("Проверка минимальных требований LEGO Batman")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    def test_lego_batman_requirements(self, driver, ui_base_url):
        with allure.step("Открытие главной страницы"):
            driver.get(ui_base_url)
        
        with allure.step("Наведение на меню Игры и выбор PC"):
            main_page = MainPage(driver)
            main_page.hover_games_and_select_pc()
        
        with allure.step("Переход на 2-ю страницу списка игр"):
            games_page = GamesPage(driver)
            games_page.go_to_page(2)
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Страница 2 списка игр",
                attachment_type=allure.attachment_type.PNG
            )
        
        with allure.step("Поиск игры LEGO Batman в списке на 2-й странице"):
            games_page = GamesPage(driver)
            game_name = "LEGO Batman: Legacy of the Dark Knight"
            assert games_page.find_game_in_list(game_name), f"Игра {game_name} не найдена"
            allure.attach(
                driver.get_screenshot_as_png(),
                name="Карточка LEGO Batman",
                attachment_type=allure.attachment_type.PNG
            )
        
        with allure.step("Проверка минимальных требований"):
            expected_requirements = {
                'os': 'Windows 11',
                'processor': 'Intel CPU Core i5-9600K',
                'ram': '16 Гб',
                'gpu': 'NVIDIA GeForce RTX 2070',
                'hdd': '50 ГБ'
            }
            game_detail = GameDetailPage(driver)
            game_detail.verify_min_requirements(expected_requirements)
    
    @allure.story("Кейс 3: Проверка скачивания CarX Drift Racing 2")
    @allure.title("Проверка кнопок скачивания CarX Drift Racing 2")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_carx_drift_racing_download(self, driver, ui_base_url):
        with allure.step("Открытие главной страницы"):
            driver.get(ui_base_url)
        
        with allure.step("Прокрутка страницы в самый низ"):
            main_page = MainPage(driver)
            main_page.scroll_to_bottom()
        
        with allure.step("Поиск игры CarX Drift Racing 2"):
            games_page = GamesPage(driver)
            game_name = "CarX Drift Racing 2"
            games_page.find_game_in_list(game_name)
        
        with allure.step("Проверка кнопок скачивания"):
            game_detail = GameDetailPage(driver)
            game_detail.verify_download_buttons()