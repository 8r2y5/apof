FROM node:7.10.0

RUN mkdir -p /opt/apof-fron
ADD . /opt/apof-fron
WORKDIR /opt/apof-fron

RUN npm install
RUN npm install -g bower
RUN npm install -g gulp
RUN bower --allow-root install

ENTRYPOINT ["gulp"]
CMD ["build"]
