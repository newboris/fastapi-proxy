# Использовать легковесный официальный образ Python
FROM python:3.12-slim

# Запретить Python писать файлы кэша .pyc на диск
ENV PYTHONDONTWRITEBYTECODE=1
# Запретить Python буферизировать логи (чтобы они сразу были видны в docker-compose)
ENV PYTHONUNBUFFERED=1

# Установить рабочую директорию внутри контейнера
WORKDIR /code

# Сначала копируем только requirements.txt (для эффективного кэширования слоев Docker)
COPY ./requirements.txt /code/requirements.txt

# Обновляем pip и устанавливаем зависимости
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /code/requirements.txt

# Копируем остальной код приложения
COPY ./app /code/app

# Команда для запуска приложения через асинхронный сервер Uvicorn
# Слушаем на порту 8000 внутри контейнера. --workers можно настроить под нагрузку
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
