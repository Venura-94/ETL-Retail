# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Playwright Python package and dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run main.py when the container launches
CMD ["python3", "ETL.py"]
