FROM python:3.11-slim

# Install system dependencies including Tesseract OCR
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    tesseract-ocr-eng \
    libtesseract-dev \
    && rm -rf /var/lib/apt/lists/*

# Set NLTK data directory environment variable
ENV NLTK_DATA=/app/nltk_data

WORKDIR /app
COPY . /app

# Create NLTK data directory with proper permissions
RUN mkdir -p /app/nltk_data && chmod 755 /app/nltk_data

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7860

# CMD ["python", "hipaathesis.py"]
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]