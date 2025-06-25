
#
# IX-API Sandbox v2 Dockerfile
#

FROM python:3.11
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
  apt-get install --no-install-recommends -y \
  git \
  inetutils-ping \
  postgresql-client \
  wkhtmltopdf && \
  rm -rf /var/lib/apt/lists/*

# Setup project
RUN mkdir -p /code
COPY . /code

WORKDIR /code
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "manage.py"]

