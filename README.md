🚀 Автоматизация тестирования игрового портала и API
🐍 Python 3.8+
🧪 Pytest 7.4.3
🌐 Selenium 4.16.0
📊 Allure
📦 GitHub Pages
📖 О проекте
Проект содержит автоматизированные тесты для:

UI — тестирование веб-сайта igrovoy.rt.ru (3 кейса)
API — тестирование сервиса управления сотрудниками (4 сценария)
Все тесты написаны с использованием Page Object Model, генерируют Allure отчеты и доступны в виде красивого веб-сайта через GitHub Pages.

🧪 Тест-кейсы
🖥️ UI Тесты (igrovoy.rt.ru)
№	Кейс	Описание
1	Поиск игры Pioner	Проверка цены 699₽
2	Проверка требований LEGO Batman	Проверка минимальных системных требований
3	Проверка скачивания CarX Drift Racing 2	Проверка наличия кнопок Google Play и App Store
⚙️ API Тесты (Управление сотрудниками)
№	Сценарий	Тип
1	Создание сотрудника	✅ Позитивный
2	Получение списка сотрудников	✅ Позитивный
3	Создание без обязательных полей	❌ Негативный
4	Получение несуществующего сотрудника	❌ Негативный
📁 Структура проекта
Rostelecom/
├── src/
│   └── ui/
│       └── pages/
│           ├── base_page.py          # Базовый класс для страниц
│           ├── main_page.py          # Главная страница
│           ├── games_page.py         # Страница с играми
│           └── game_detail_page.py   # Страница деталей игры
├── tests/
│   ├── api/
│   │   └── test_employee_api.py      # API тесты
│   └── ui/
│       └── test_games.py             # UI тесты
├── docs/
│   ├── index.html                    # Главная страница с отчетами
│   ├── ui-report/                    # Allure отчет UI
│   └── api-report/                   # Allure отчет API
├── drivers/
│   └── chrome/
│       └── chromedriver.exe          # ChromeDriver
├── conftest.py                       # Фикстуры pytest
├── pytest.ini                        # Конфигурация pytest
├── requirements.txt                  # Зависимости
└── README.md                         # Документация
        
🛠️ Установка и запуск
1. Клонирование репозитория
git clone https://github.com/ВАШ_НИК/rostelecom-tests.git
cd rostelecom-tests
2. Создание виртуального окружения
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux
3. Установка зависимостей
pip install -r requirements.txt
4. Запуск UI тестов
pytest -m ui -v
5. Запуск API тестов
pytest -m api -v
6. Запуск всех тестов с Allure
pytest --alluredir=allure-results -v
allure serve allure-results
📊 Отчеты Allure
Отчеты доступны онлайн по ссылке:
🔗 https://ВАШ_НИК.github.io/rostelecom-tests/docs/

Локальный просмотр:

# UI отчет
allure open docs/ui-report

# API отчет
allure open docs/api-report
🧰 Используемые технологии
Технология	Назначение
Python 3.8+	Язык программирования
Pytest	Фреймворк для тестирования
Selenium WebDriver	Автоматизация браузера
Allure	Генерация отчетов
Requests	API тестирование
Page Object Model	Архитектура проекта
GitHub Pages	Хостинг отчетов
📝 Примечания
⚠️ API сервис на фиксе возвращает ошибку 500 (внутренняя ошибка сервера). Тесты написаны корректно и будут работать после восстановления сервиса.
🧪 Все UI тесты успешно проходят.
📊 Allure отчеты сгенерированы и доступны онлайн.
🤝 Вклад в проект
Сделайте форк репозитория
Создайте ветку для фичи (git checkout -b feature/NewFeature)
Зафиксируйте изменения (git commit -m 'Add new feature')
Отправьте изменения (git push origin feature/NewFeature)
Откройте Pull Request
📄 Лицензия
MIT License — свободное использование, копирование, модификация.

📧 Контакты
Автор: Ваше Имя
GitHub: https://github.com/ВАШ_НИК