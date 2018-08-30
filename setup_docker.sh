#!/usr/bin/env bash

# Apply database migrations

echo "Apply database migrations"
docker-compose exec app python manage.py makemigrations
docker-compose exec app python manage.py migrate
docker-compose exec app python manage.py loaddata initial_data.json
docker-compose exec app python manage.py collectstatic --no-input