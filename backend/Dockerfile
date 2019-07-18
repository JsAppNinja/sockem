FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /app/backend
WORKDIR /app/backend
COPY requirements.txt /app/backend/
RUN pip install -r requirements.txt
COPY . .
COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]