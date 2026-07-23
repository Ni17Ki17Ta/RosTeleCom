import random
from faker import Faker

fake = Faker('ru_RU')

def generate_valid_employee():
    """Генерирует валидные данные для сотрудника."""
    return {
        "name": fake.name(),
        "email": fake.email(),
        "position": fake.job(),
        "department": random.choice(["IT", "HR", "Finance", "Marketing", "Sales"]),
        "company": fake.company(),
        "salary": random.randint(50000, 200000)
    }

def generate_minimal_valid_employee():
    """Генерирует минимальные валидные данные (только name и salary)."""
    return {
        "name": fake.name(),
        "salary": random.randint(50000, 200000)
    }

def generate_invalid_employee():
    """Генерирует невалидные данные."""
    return {
        "name": "",
        "email": "invalid_email",
        "position": "",
        "department": "",
        "company": "",
        "salary": -1000
    }