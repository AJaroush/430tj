# Lightweight Python image
FROM python:3.12-slim

# Prevent Python from writing .pyc & buffering stdout
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Workdir inside the container
WORKDIR /app

# System packages (curl for health checks/logs if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
 && rm -rf /var/lib/apt/lists/*

# Install Python deps first (better layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project
COPY . .

# Expose Django dev port
EXPOSE 8000

# For dev we’ll just run the Django server.
# For production you’d switch to gunicorn and a real DB.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
