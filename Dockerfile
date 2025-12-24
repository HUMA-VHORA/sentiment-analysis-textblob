FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && python -m textblob.download_corpora

COPY app.py .

CMD ["python", "app.py"]
