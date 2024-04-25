# Приложение на FastAPI

### Технологии
* Python 
* FastAPI
* SQLAlchemy
* Alembic

### Как запустить проект:

+ Клонировать репозиторий и перейти в него в командной строке:

  ```
  git clone git@github.com:dimn3/.git
  ```

  ```
  cd cat_charity_fund
  ```

+ Cоздать и активировать виртуальное окружение:

  ```
  python -m venv venv
  ```
  ```
  source venv/scripts/activate
  ```

* Установить зависимости из файла requirements.txt:

  ```
  python -m pip install --upgrade pip
  ```

  ```
  pip install -r requirements.txt
  ```

* Создать переменные окружения (файл .env). Пример заполнения файла:
  ```
  APP_TITLE=Название
  DESCRIPTION=Описание
  DATABASE_URL=SQLITE+AIOSQLITE:///./FASTAPI.DB
  SECRET=SECRET
  FIRST_SUPERUSER_EMAIL=test@test.ru
  FIRST_SUPERUSER_PASSWORD=password
  ```
* Применить миграции:

  ```
  alembic upgrade head
  ```

* Запуск проекта:

  ```
  uvicorn app.main:app
  ```

---
