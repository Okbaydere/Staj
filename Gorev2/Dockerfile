FROM python:3.9
LABEL version="1.0" \
     maintainer="Oğuz Kaan" \
     maintainer.mail="okbaydere@gmail.com"
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["website/models.py"]
CMD ["python","main.py"]



