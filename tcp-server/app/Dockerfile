FROM python:3.11.4-slim

#MAINTAINER Alex Mattson "alex.mattson@gmail.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
  wget && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./server.py /app 

RUN addgroup --system appuser && adduser --system appuser --ingroup appuser
USER appuser

ENTRYPOINT [ "python" ]

CMD [ "server.py" ]
