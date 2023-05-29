FROM python:3.11-alpine

ADD requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

# Copy local code to the container image.
ENV APP_HOME /var/server
WORKDIR $APP_HOME
COPY . ./

# ADD app.py /var/server/app.py

CMD python /var/server/app.py