FROM python:3.10

WORKDIR /workspace

COPY requirements.txt .

RUN pip install -U pip \
    && pip install --no-cache-dir --upgrade -r requirements.txt