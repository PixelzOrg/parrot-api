FROM public.ecr.aws/lambda/python:3.10

# Install necessary system packages
RUN yum -y install git wget tar xz

# Install FFMPEG
RUN wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz && \
    tar xvf ffmpeg-release-amd64-static.tar.xz && \
    mv ffmpeg-6.1-amd64-static/ffmpeg /usr/bin/ffmpeg && \
    rm -Rf ffmpeg*

# Copy the requirements.txt file and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Whisper
RUN pip install --no-cache-dir git+https://github.com/openai/whisper.git 

# Preload Whisper model (optional)
RUN whisper --model_dir /usr/local --model medium audio >> /dev/null 2>&1; exit 0

# Copy your application code
COPY src/ ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler
CMD ["src.handler"]
