FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD bash -c 'while !</dev/tcp/db/5432; do sleep 1; done; python ./backend/manage.py runserver 0.0.0.0:8000'