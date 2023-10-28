# # Use an official Python runtime as a parent image
# FROM python:3.8

# # Set the working directory to /app
# WORKDIR /app

# # Copy the current directory contents into the container at /app
# COPY . /app

# # Install any needed packages specified in requirements.txt
# RUN pip install -r requirements.txt

# # Make port 5432 available to the world outside this container
# EXPOSE 5432

# # Define environment variables for PostgreSQL
# ENV POSTGRES_DB=sicredi_data_challenge
# ENV POSTGRES_USER=sicredi
# ENV POSTGRES_PASSWORD=postgresql

# # Command to run your application
# CMD ["python", "src/main.py"]

# FROM datamechanics/spark:3.2.1-hadoop-3.3.1-java-11-scala-2.12-python-3.8-dm18

# USER root

# WORKDIR /app

# RUN pip install --upgrade pip

# COPY . /app
# RUN pip3 install -r requirements.txt

# CMD jupyter-lab --allow-root --no-browser --ip=0.0.0.0
FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y default-jdk scala wget vim software-properties-common python3.8 python3-pip curl unzip libpq-dev build-essential libssl-dev libffi-dev python3-dev && \
    apt-get clean

RUN wget https://archive.apache.org/dist/spark/spark-3.0.1/spark-3.0.1-bin-hadoop3.2.tgz && \
    tar xvf spark-3.0.1-bin-hadoop3.2.tgz && \
    mv spark-3.0.1-bin-hadoop3.2/ /usr/local/spark && \
    ln -s /usr/local/spark spark && \
    wget https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.11.890/aws-java-sdk-bundle-1.11.890.jar && \
    mv aws-java-sdk-bundle-1.11.890.jar /spark/jars && \
    wget https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.2.0/hadoop-aws-3.2.0.jar && \
    mv hadoop-aws-3.2.0.jar /spark/jars

# Add the PostgreSQL JDBC driver
RUN wget https://jdbc.postgresql.org/download/postgresql-42.2.23.jar -O /spark/jars/postgresql-42.2.23.jar

WORKDIR /app
COPY . /app

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ENV PYSPARK_PYTHON=python3
ENV PYSPARK_SUBMIT_ARGS='--packages io.delta:delta-core_2.12:0.8.0,org.postgresql:postgresql:42.2.23 pyspark-shell'
