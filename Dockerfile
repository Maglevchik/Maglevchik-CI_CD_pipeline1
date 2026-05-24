# Используем официальный легковесный образ Python
FROM python:3.10-slim

# Устанавливаем рабочую папку внутри контейнера
WORKDIR /app

# Запрещаем создание лишних кэш-файлов для экономии места
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Устанавливаем системные пакеты, нужные для корректной сборки PostgreSQL
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

# Копируем список зависимостей и устанавливаем их
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь написанный тобой код в контейнер
COPY . /app/

# Запускаем проект через gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "bot_builder.wsgi:application"]