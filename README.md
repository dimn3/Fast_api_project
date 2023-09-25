# Приложение для Благотворительного фонда поддержки котиков QRKot

Фонд собирает пожертвования на различные целевые проекты: на медицинское обслуживание нуждающихся хвостатых, 
на обустройство кошачьей колонии в подвале, на корм оставшимся без попечения кошкам — на любые цели, связанные с 
поддержкой кошачьей популяции.

### Технологии
* Python 
* FastAPI
* SQLAlchemy
* Alembic

### Как запустить проект:

+ Клонировать репозиторий и перейти в него в командной строке:

  ```
  git clone git@github.com:dimn3/cat_charity_fund.git
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

* Создать переменные окружения (файл cat_charity_fund/.env). Пример заполнения файла:
  ```
  APP_TITLE=QRKot
  DESCRIPTION=Фонд поддержки котиков
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