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
RUN mkdir -p /app/nltk_data && chmod 777 /app/nltk_data

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK data during build
RUN python -c "import nltk; nltk.download('punkt', download_dir='/app/nltk_data'); nltk.download('punkt_tab', download_dir='/app/nltk_data'); nltk.download('stopwords', download_dir='/app/nltk_data'); nltk.download('wordnet', download_dir='/app/nltk_data'); nltk.download('omw-1.4', download_dir='/app/nltk_data')"

# Create log directory with proper permissions
RUN mkdir -p /app/logs && chmod 777 /app/logs

EXPOSE 7860

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]