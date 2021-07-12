FROM python:3
WORKDIR /home/codes
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
