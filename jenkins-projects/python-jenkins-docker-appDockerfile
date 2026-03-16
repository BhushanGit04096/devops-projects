FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependency file first for better Docker layer caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY . .

# Run the application
CMD ["python", "app.py"]
