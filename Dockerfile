FROM alpine
RUN apk update && \
    apk upgrade && \
    apk add python3 && \
    pip3 install --upgrade pip && \
    pip3 install flask
WORKDIR /opt/exampleapp
COPY . .
EXPOSE 5000
CMD flask run

