import requests
from src.api.clients.base_api_client import BaseApiClient

EMPLOYEES_ENDPOINT = "/api/employees"

class EmployeeClient(BaseApiClient):
    """API-клиент для работы с сотрудниками."""

    def get_all_employees(self) -> requests.Response:
        return self.get(EMPLOYEES_ENDPOINT)

    def get_employee(self, employee_id: int) -> requests.Response:
        return self.get(f"{EMPLOYEES_ENDPOINT}/{employee_id}")

    def create_employee(self, employee_data: dict) -> requests.Response:
        return self.post(EMPLOYEES_ENDPOINT, json_body=employee_data)

    def update_employee(self, employee_id: int, employee_data: dict) -> requests.Response:
        return self.put(f"{EMPLOYEES_ENDPOINT}/{employee_id}", json_body=employee_data)

    def patch_employee(self, employee_id: int, employee_data: dict) -> requests.Response:
        return self.patch(f"{EMPLOYEES_ENDPOINT}/{employee_id}", json_body=employee_data)

    def delete_employee(self, employee_id: int) -> requests.Response:
        return self.delete(f"{EMPLOYEES_ENDPOINT}/{employee_id}")