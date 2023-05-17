FROM python:3.8-slim-buster

WORKDIR /home/app/

COPY ./ /home/app/

RUN pip install -r requirements.txt

ENV PYTHONPATH=${PYTHONPATH}:/home/app/

ENV level="debug"


VOLUME /home/app/data/

CMD ["bash", "-c", "gunicorn main:app -b 0.0.0.0:5000"]
