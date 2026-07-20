# 🚀 Rostelecom — автоматизация тестирования

Проект объединяет UI- и API-автотесты в едином репозитории:

- **UI** — проверка витрины [igrovoy.rt.ru](https://igrovoy.rt.ru/): каталог игр, карточка товара, системные требования, ссылки на скачивание.
- **API** — проверка сервиса управления сотрудниками (`http://185.193.143.49:8080/swagger-ui/index.html#/`): создание, получение и обработка ошибок.

Стек: **Python + Pytest + Selenium + Requests + Allure**. UI-часть построена по паттерну **Page Object Model**, тесты запускаются в Google Chrome.

---

## 📋 Требования

Перед запуском убедитесь, что установлено:

| Инструмент | Версия | Зачем нужен |
|---|---|---|
| Python | 3.8+ | запуск тестов |
| Google Chrome | последняя стабильная | UI-тесты (Selenium) |
| Allure Commandline | любая актуальная | просмотр отчётов |
| Docker Desktop | опционально | локальный запуск API-сервиса |

Проверить, что Allure установлен:

```bash
allure --version
```

Установить зависимости проекта:

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🖥️ UI-тесты

Тесты находятся в `tests/ui/`, страницы (Page Object) — в `src/ui/pages/`. Драйвер Chrome лежит в `drivers/chrome/chromedriver.exe` и настраивается один раз в `conftest.py`.

Запуск:

```bash
python -m pytest tests/ui --clean-alluredir --alluredir=allure-results
allure serve allure-results
```

Headless-режим (без открытия окна браузера):

```bash
HEADLESS=1 python -m pytest tests/ui --clean-alluredir --alluredir=allure-results
```

### Покрытые сценарии

| № | Кейс | Что проверяется |
|---|---|---|
| 1 | Поиск игры **Pioner** | Цена в карточке товара соответствует **699 ₽** |
| 2 | Игра **LEGO Batman: Legacy of the Dark Knight** | Минимальные требования: Windows 11, Intel Core i5-9600K, 16 ГБ RAM, NVIDIA GeForce RTX 2070, 50 ГБ на диске |
| 3 | Игра **CarX Drift Racing 2** | В блоке «Скачать игру» присутствуют ссылки на **Google Play** и **App Store** |

---

## ⚙️ API-тесты

Тесты находятся в `tests/api/`. По умолчанию используется удалённый стенд:

```
http://185.193.143.49:8080
```

Если стенд доступен, запуск стандартный:

```bash
python -m pytest tests/api --clean-alluredir --alluredir=allure-results
allure serve allure-results
```

### Покрытые сценарии

| Сценарий | Тип | Ожидаемый результат |
|---|---|---|
| Создание сотрудника | ✅ позитивный | сотрудник успешно создан, код ответа 200/201 |
| Получение списка сотрудников | ✅ позитивный | возвращается список, код ответа 200 |
| Создание без обязательных полей | ❌ негативный | сервис отклоняет запрос, код ответа 400 |
| Получение несуществующего сотрудника | ❌ негативный | сервис возвращает 404 |

### Локальный запуск сервиса через Docker

Если удалённый стенд недоступен, сервис можно поднять локально из отдельного репозитория:

```bash
git clone https://github.com/mxmrbkv/training_swagger.git
cd training_swagger
chmod +x gradlew
./gradlew build
docker compose up --build -d
```

После запуска Swagger будет доступен по адресу `http://localhost:8080/swagger-ui/index.html`.

> На Mac с Apple Silicon в `Dockerfile` может потребоваться заменить образы `eclipse-temurin:17-jdk-alpine` / `eclipse-temurin:17-jre-alpine` на `eclipse-temurin:17-jdk` / `eclipse-temurin:17-jre`.

Затем в новом терминале запускаете тесты с указанием локального адреса:

```bash
EMPLOYEE_API_BASE_URL=http://localhost:8080 python -m pytest tests/api --clean-alluredir --alluredir=allure-results
allure serve allure-results
```

Остановить локальный сервис:

```bash
cd training_swagger
docker compose down
```

---

## 🏷️ Запуск отдельных групп тестов

Тесты размечены маркерами `positive` и `negative` — можно запускать выборочно:

```bash
python -m pytest -m positive
python -m pytest -m negative
```

Флаг `--clean-alluredir` очищает результаты предыдущего прогона, поэтому в отчёте всегда только актуальные тесты.

---

## 📊 Allure-отчёт

Быстрый просмотр отчёта сразу после прогона:

```bash
allure serve allure-results
```

Сохранить статический HTML-отчёт (например, для публикации):

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

Готовые отчёты в этом репозитории также опубликованы через GitHub Pages и лежат в `docs/ui-report` и `docs/api-report`.

---

## 📁 Структура проекта

```
Rostelecom/
├── src/
│   └── ui/
│       └── pages/
│           ├── base_page.py         # базовые методы работы с элементами
│           ├── main_page.py         # главная страница, меню, поиск
│           ├── games_page.py        # каталог игр
│           └── game_detail_page.py  # карточка игры
├── tests/
│   ├── api/
│   │   └── test_employee_api.py     # позитивные и негативные API-сценарии
│   └── ui/
│       └── test_games.py            # 3 UI-кейса
├── docs/
│   ├── index.html                   # лендинг с отчётами (GitHub Pages)
│   ├── ui-report/                   # сгенерированный Allure-отчёт (UI)
│   └── api-report/                  # сгенерированный Allure-отчёт (API)
├── drivers/
│   └── chrome/
│       └── chromedriver.exe         # драйвер для Selenium
├── conftest.py                      # общие фикстуры (запуск браузера и др.)
├── pytest.ini                       # конфигурация pytest и маркеры
├── requirements.txt
└── README.md
```

---

## 📄 Примечание об API

На момент подготовки проекта удалённый стенд `185.193.143.49:8080` находится «на фиксе» и отвечает ошибкой **500** на часть запросов. API-тесты написаны и корректно проверяют бизнес-логику сервиса — падения в отчёте связаны исключительно с недоступностью стенда, а не с ошибками в тестах. Для проверки работоспособности тестов рекомендуется либо дождаться восстановления стенда, либо поднять сервис локально через Docker (см. раздел выше).

---

## ✍️ Автор и лицензия

Проект подготовлен в рамках практики по автоматизации тестирования (Ростелеком).

Лицензия: MIT — свободно используйте и модифицируйте код проекта.
