FROM python:3.7-alpine

COPY bot/tweet.py /bot/
COPY bot/opensea.py /bot/
COPY bot/config.py /bot/
COPY files files/
COPY templates/successful.txt templates/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bot
CMD ["python3", "tweet.py"]