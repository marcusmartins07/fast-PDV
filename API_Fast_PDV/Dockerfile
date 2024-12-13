FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "python manage.py makemigrations produto && \
                   python manage.py makemigrations usuarios && \
                   python manage.py makemigrations pedido && \
                   python manage.py migrate && \
                   python manage.py shell -c 'from usuarios.bd_backup import insert_bd; insert_bd()' && \
                   python manage.py runserver 0.0.0.0:8000"]
