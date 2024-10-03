
FROM python:3.10-bookworm

# Update the image and install basics
RUN apt-get update && \
    apt-get install -y sudo git git-lfs nano python3-pip software-properties-common build-essential wget curl build-essential gcc make

# Required by subnet:
RUN apt-get install -y ffmpeg

# Added to speed up docker build using cache.  Makes our pipelines MUCH faster
RUN pip3 install torch torchaudio

# Copy repo into /app folder
COPY . /app

# Set working directory
WORKDIR /app/

# Install the required python packages
RUN pip3 install -r requirements.txt

# Set the entrypoint to Python and pass the script and additional options as arguments
ENTRYPOINT ["python3"]

# The default script, but it will be overridden if arguments are passed
CMD ["neurons/miner.py"]