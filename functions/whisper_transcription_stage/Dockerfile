FROM public.ecr.aws/lambda/python:3.10


COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.txt 
RUN yum -y install git wget tar xz
RUN wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz && tar xvf ffmpeg-release-amd64-static.tar.xz && mv ffmpeg-6.1-amd64-static/ffmpeg /usr/bin/ffmpeg && rm -Rf ffmpeg*
RUN pip install setuptools-rust
RUN pip install git+https://github.com/openai/whisper.git
RUN pip install -r requirements.txt 

COPY src/ ${LAMBDA_TASK_ROOT}

CMD [ "main.handler" ]