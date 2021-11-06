
FROM pandoc/latex:2.16.1

RUN apk add python3 py3-pip

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
