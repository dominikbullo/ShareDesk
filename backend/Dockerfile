FROM python:3.10

# python envs
ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

COPY ./Pipfile* /

# Install pipenv
RUN pip install --upgrade pip
RUN pip install pipenv

RUN pipenv lock --requirements > requirements.txt
RUN pip install -r requirements.txt

#Instal also dev packpages
RUN pipenv lock --dev --requirements > requirements_dev.txt
RUN pip install -r requirements_dev.txt

# upload scripts
COPY ./scripts/entrypoint.sh ./scripts/start.sh ./scripts/gunicorn.sh /

# Fix windows docker bug, convert CRLF to LF
RUN sed -i 's/\r$//g' /start.sh && chmod +x /start.sh &&\
    sed -i 's/\r$//g' /entrypoint.sh && chmod +x /entrypoint.sh &&\
    sed -i 's/\r$//g' /gunicorn.sh && chmod +x /gunicorn.sh

WORKDIR /app
