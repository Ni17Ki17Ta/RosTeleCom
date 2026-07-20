import pytest
import allure
import requests
import json

@allure.epic("API Тестирование")
@allure.feature("Управление сотрудниками")
class TestEmployeeAPI:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.base_url = "http://185.193.143.49:8080"
        self.employee_endpoint = f"{self.base_url}/api/employees"
        self.headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
    
    @allure.story("Позитивные сценарии")
    @allure.title("Создание нового сотрудника")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.api
    def test_create_employee(self):
        employee_data = {
            "name": "Иван Иванов",
            "email": "ivan@example.com",
            "position": "Java Developer",
            "department": "Разработка",
            "company": "Acme Corp",
            "salary": 100000
        }
        
        with allure.step("Отправка POST запроса"):
            response = requests.post(
                self.employee_endpoint,
                json=employee_data,
                headers=self.headers
            )
            print(f"\n📤 Статус ответа: {response.status_code}")
            print(f"📥 Тело ответа: {response.text}")
        
        with allure.step("Проверка статуса ответа"):
            # Если сервер возвращает 500, но мы знаем, что он работает через Swagger
            # Возможно, это тестовый сервер, который всегда возвращает 500
            # Проверяем, что статус либо 201, либо 500 (если сервер на фиксе)
            assert response.status_code in [201, 200], f"Ожидался 201 или 200, получен {response.status_code}"