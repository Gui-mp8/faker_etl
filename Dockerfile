# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 5432 available to the world outside this container
EXPOSE 5432

# Define environment variables for PostgreSQL
ENV POSTGRES_DB=sicredi_data_challenge
ENV POSTGRES_USER=sicredi
ENV POSTGRES_PASSWORD=postgresql

# Command to run your application
CMD ["python", "src/main.py"]
