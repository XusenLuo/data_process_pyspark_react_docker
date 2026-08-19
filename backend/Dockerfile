FROM python:3.11-bookworm

# Install Java 17 for PySpark
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        openjdk-17-jdk-headless \
    && rm -rf /var/lib/apt/lists/*

# Configure Java
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

# Configure PySpark to use this Python
ENV PYSPARK_PYTHON=/usr/local/bin/python
ENV PYSPARK_DRIVER_PYTHON=/usr/local/bin/python

WORKDIR /app/backend

# Install Python dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy application and tests
COPY src ./src
COPY tests ./tests

ENV PYTHONPATH=/app/backend/src

# Run all unit tests
CMD ["python", "src/main.py", "-m", "unittest", "tests/test_*.py"]