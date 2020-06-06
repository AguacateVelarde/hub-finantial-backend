FROM tiangolo/uwsgi-nginx-flask:python3.8
ARG BELVO_SECRET_ID 
ARG BOLVO_SECRET_PASSWORD

ENV BELVO_SECRET_ID $BELVO_SECRET_ID
ENV BOLVO_SECRET_PASSWORD $BOLVO_SECRET_PASSWORD

COPY ./finiahub/ /app

RUN pip install -r requirements.txt