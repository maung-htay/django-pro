docker-compose exec rm -r books/migrations
docker-compose exec python manage.py makemigrations books
docker-compose exec python manage.py migrate
docker-compose exec python manage.py createsuperuser
docker-compose exec python manage.py collectstatic

docker volume ls
docker volume rm django-docker_postgres_data