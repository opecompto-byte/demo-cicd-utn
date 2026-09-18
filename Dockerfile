FROM python:3.9-slim

WORKDIR /app

# Instalamos las dependencias primero para optimizar la caché de Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el código fuente y los tests
COPY . .

EXPOSE 5000
CMD ["python", "app.py"]