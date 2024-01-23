FROM python:3.9

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt 

RUN pip install git+https://github.com/openai/whisper.git

COPY src/ /app/

CMD ["python", "./main.py"]
