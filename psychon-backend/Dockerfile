FROM python:3.11-slim

# Install git to clone the artifacts
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy only the backend code (without artifacts)
COPY backend/ /app/

# Clone the main GitHub repo (which contains the artifacts) into a temp folder
RUN git clone --depth 1 https://github.com/Psycho1234567890/PSYCHON.git /tmp/psychon

# Copy the artifacts from the cloned repo into the app folder
RUN cp -r /tmp/psychon/backend/artifacts /app/artifacts

# Clean up temp folder
RUN rm -rf /tmp/psychon

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 7860

CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app"]