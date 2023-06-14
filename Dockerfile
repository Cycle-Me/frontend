# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt /app

# Install the project dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY assets /app/assets

COPY index.html /app

# Copy the application code to the working directory
COPY . .

EXPOSE 8080

# Set the entry point to the Flask application
CMD ["python", "feedback_api.py"]