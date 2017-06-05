FROM python:3

WORKDIR /root/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install pika
COPY . .

CMD [ "python","-u","./src/main/process.py" ]
