FROM postgres:14

RUN apt-get update
RUN apt-get install postgresql-14-q3c postgresql-contrib -yqq

# This init script is only run once at first run of the container.
COPY ./init-db.sh /docker-entrypoint-initdb.d/init-db.sh