
FROM python:3.8

WORKDIR /main

COPY ./src ./src

COPY ./data/data.csv ./src/data.csv

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

CMD ["python3","./src/main.py"]
