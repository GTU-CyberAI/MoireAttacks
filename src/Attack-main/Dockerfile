# Use the latest Ubuntu image
FROM ubuntu:latest

# Label the image
LABEL authors="huskoc"

# Set working directory
WORKDIR /app

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    apt-get clean

# Copy the requirements file
COPY requirements.txt /app/

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . /app/

# Run a Python script (replace 'main.py' with your actual script)
ENTRYPOINT ["python3", "Moire_Attack.py"]
