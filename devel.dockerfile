FROM python:2.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /opt/apof/
ADD . /opt/apof/
WORKDIR /opt/apof/

RUN pip install -U pip
RUN pip install -I -e .[develop] --process-dependency-links

WORKDIR /opt/apof/src/apof
ENTRYPOINT ["apofcmd"]
CMD ["django","runserver","0.0.0.0:8000"]
