FROM ubuntu:latest
MAINTAINER Rietesh "rietesh4535@gmail.com"
RUN apt-get update -y
RUN apt-get install -y python3-pip python3-dev build-essential libsm6 libxext6 libxrender-dev
COPY . /image_classifier
WORKDIR /image_classifier
RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
