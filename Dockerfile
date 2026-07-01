# Use Python 3.11 (TensorFlow compatible)
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only the backend folder into the container
COPY backend/ /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port HF Spaces uses
EXPOSE 7860

# Start Gunicorn (production server)
CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app"]