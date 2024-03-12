FROM python:3.8

# Copy files over for building the container
RUN mkdir /gleam_webapp
WORKDIR /gleam_webapp
COPY ./entrypoint.sh /gleam_webapp/.
COPY ./requirements.txt /gleam_webapp/.

# Install necessary packages
RUN apt-get update
RUN apt-get install postgresql libpq-dev python3.8-dev graphviz python3-pip locales -yqq

# Install Python requirements
RUN pip3 install uwsgi
RUN pip3 install -r requirements.txt

# Start the container with entrypoint script
ENTRYPOINT ["/gleam_webapp/entrypoint.sh"]