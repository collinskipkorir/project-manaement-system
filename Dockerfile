FROM python:3.9

ENV APP_HOME=/home/projement
RUN mkdir $APP_HOME

# set work directory
WORKDIR $APP_HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /home/projement/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . $APP_HOME

RUN chmod +x $APP_HOME/entrypoint.sh