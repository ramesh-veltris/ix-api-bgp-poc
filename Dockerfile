
#
# IX-API BGP POC Dockerfile
#

FROM python:3.11
ENV PYTHONUNBUFFERED 1

# Setup project
RUN mkdir -p /code
COPY . /code

WORKDIR /code
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "manage.py"]

