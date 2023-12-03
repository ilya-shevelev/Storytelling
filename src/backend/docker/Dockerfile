FROM python:3.12-slim-bullseye

ENV DJANGO_ENV=${DJANGO_ENV} \
    # python:
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    # pip:
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Copy only requirements, to cache them in docker layer
WORKDIR /app
COPY ./requirements.txt /app/

# System dependencies:
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    build-essential gettext libpq-dev wget curl \
    # Cleaning cache:
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/* \
    # Installing requirements
    && pip install -r requirements.txt

# Creating folders, and files for a project:
COPY . /app/
COPY docker/entrypoint.sh /entrypoint.sh

# Setting up proper permissions:
RUN chmod +x /entrypoint.sh \
    && mkdir -p /app/media /app/static \
    && chmod +x /app/media/ /app/static/
