FROM hypriot/rpi-alpine-scratch

RUN apk update && \
apk upgrade && \
apk add python py-pip && \
rm -rf /var/cache/apk/*

RUN pip install rxv

EXPOSE 8080
ADD server.py /app/server.py

CMD ["python", "/app/server.py"]
