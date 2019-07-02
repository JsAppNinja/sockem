#!/usr/bin/env bash

while !</dev/tcp/db/5432; do sleep 1; done;

echo "running python ./backend/manage.py makemigrations"
python ./backend/manage.py makemigrations

echo "running python ./backend/manage.py migrate"
python ./backend/manage.py migrate

echo "running python script for superuser"
echo "
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.create_superuser('admin', 'admin@sockemboppem.com', 'password')
" | python ./backend/manage.py shell

python ./backend/manage.py runserver 0.0.0.0:8000