# PostgreSQL Example Application

Это простое приложение на Python, которое демонстрирует подключение к базе данных PostgreSQL, создание таблицы, вставку данных и извлечение данных. Приложение использует библиотеку `psycopg2` для работы с PostgreSQL.

## Установка

### Требования

- Python 3.x
- Docker
- Docker Compose

### Настройка окружения

Перед запуском приложения убедитесь, что у вас установлены необходимые переменные окружения для подключения к базе данных PostgreSQL. 

- POSTGRES_DATABASE=your_database_name
- POSTGRES_USER=your_username
- POSTGRES_PASSWORD=your_password
- POSTGRES_HOSTNAME=db
- POSTGRES_PORT=5432