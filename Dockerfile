FROM ubuntu:latest
WORKDIR /app
COPY dockertest.py /app
CMD sudo apt install python3
CMD pip3 install requests
RUN ['python3', 'dockertest.py']