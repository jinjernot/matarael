FROM python:3.9

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 80

ENV NAME matarael_env

CMD [ "python", "main.py" ]

