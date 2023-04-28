FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y git \
    && pip install .

ENTRYPOINT ["woothook"]

CMD ["example.config"]
