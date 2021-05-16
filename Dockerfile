FROM python:3.7-alpine

RUN pip install celery redis django

WORKDIR app/proj

#CMD [ "celery","-A proj","worker","-l info","-E" ]  
ENTRYPOINT [ "celery" ]