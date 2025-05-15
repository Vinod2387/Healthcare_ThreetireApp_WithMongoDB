# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy dependency list
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files into container
COPY . .

# Set environment variables (optional but helpful)
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV MONGO_URI=mongodb://mongo:27017/healthcare

# Expose port for Flask
EXPOSE 5000

# Start Flask app
CMD ["flask", "run"]
