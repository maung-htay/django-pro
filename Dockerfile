# build image for python
FROM python:3.10.4-slim-bullseye

# set ENV variable
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set Work directory
WORKDIR /code

# copy requirements.txt
COPY ./requirements .
RUN pip install -r requirements.txt

# copy project 
COPY . .

