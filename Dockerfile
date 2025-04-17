FROM ubuntu:latest

MAINTAINER authors="zhangguangde"

RUN mkdir "/app" 

WORKDIR /app

COPY . /app

CMD ["top", "-b"]