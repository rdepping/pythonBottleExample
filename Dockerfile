# A super-simple bottle server that exposes port 8080
FROM alpine

# install pip and hello-world server requirements
RUN apk add --update \
    python \
    python-dev \
    py-pip \
    build-base \
  && pip install virtualenv \
  && rm -rf /var/cache/apk/*

WORKDIR /home/bottle/

ADD requirements.txt requirements.txt
ADD server.py server.py
ADD sqlCreate.py sqlCreate.py
ADD views/ views/

RUN pip install -r requirements.txt
RUN python sqlCreate.py

EXPOSE 8080
ENTRYPOINT ["/usr/bin/python", "/home/bottle/server.py"]
