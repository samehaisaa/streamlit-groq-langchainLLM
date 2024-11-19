# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set a working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container
COPY . .

# Expose the port the app will run on
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "app.py"]
