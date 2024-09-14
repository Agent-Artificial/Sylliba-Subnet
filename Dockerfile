
# Use the official image as a parent image
FROM ubuntu:22.04

# Update the image and install basics
RUN apt-get update && \
    apt-get install -y sudo git git-lfs nano python3.11 python3-pip software-properties-common build-essential wget curl build-essential gcc make

# Copy repo into /app folder
COPY . /app

# Set working directory
WORKDIR /app/

# Install the required python packages
RUN pip3 install -r requirements.txt

# Set the entrypoint to Python and pass the script and additional options as arguments
ENTRYPOINT ["python3"]

# The default script, but it will be overridden if arguments are passed
CMD ["neurons/miner.py", "--logging.debug"]