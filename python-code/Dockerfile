# Use a lightweight Python image
FROM python:3.11-slim

ARG AZURE_STORAGE_ACCOUNT_NAME
ENV AZURE_STORAGE_ACCOUNT_NAME=${AZURE_STORAGE_ACCOUNT_NAME}
ARG AZURE_STORAGE_CONTAINER_NAME
ENV AZURE_STORAGE_CONTAINER_NAME=${AZURE_STORAGE_CONTAINER_NAME}
# Prevent .pyc files and enable real-time output
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . /app

# Run the app
CMD ["python", "-u", "app.py"]
