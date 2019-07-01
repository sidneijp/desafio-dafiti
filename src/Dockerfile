FROM python:3.7-alpine
LABEL maintainer="Sidnei Pereira <sidi.jp@gmail.com>" \
      description="Django Application container image meant for development"

RUN pip install pipenv pip setuptools -U
RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc postgresql-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev

# Create user inside container that matches the same UID and GID (from .env file) of the user
# building the image. It helps with permission issues when mounting volumes so it can write to
# disk inside or outside the container (since the same user that build it also run it)
ARG DOCKER_GROUP_ID
ARG DOCKER_USER_ID
ENV DOCKER_GROUP_ID=$DOCKER_GROUP_ID
ENV DOCKER_USER_ID=$DOCKER_USER_ID

RUN addgroup -g $DOCKER_GROUP_ID -S $DOCKER_GROUP_ID \
    && adduser -u $DOCKER_USER_ID -S -G $DOCKER_GROUP_ID $DOCKER_USER_ID \
    && mkdir -p /code \
    && chown $DOCKER_USER_ID:$DOCKER_GROUP_ID -R /code

WORKDIR /code

USER $DOCKER_USER_ID

ADD Pipfile.lock /code/
ADD Pipfile /code/

RUN pipenv sync --dev

# TODO: Consider remove this step and the last one (CMD ..,) to save build time since this image is meant to development
ADD . /code/

ENTRYPOINT ["pipenv", "run"]

EXPOSE 8000/tcp

CMD ["python", "/code/manage.py", "runserver", "0.0.0.0:8000"]
