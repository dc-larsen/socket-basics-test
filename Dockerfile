FROM python:3.11-slim

WORKDIR /app

# Install some packages with known vulnerabilities for testing
RUN pip install requests==2.25.0 flask==2.0.0

COPY . .

CMD ["python", "app.py"]
