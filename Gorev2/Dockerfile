FROM python:3.9
COPY requirements.txt /
RUN pip install -r /requirements.txt
RUN pip install mysqlclient
COPY . /app
WORKDIR /app
EXPOSE 5000
CMD [ "python", "main.py" ]