localserver:
	python3 manage.py runserver --settings=projement.setting_test

setup:
	docker-compose up -d --build

dropcontainer:
	docker-compose down -v

migrate:
	 docker-compose exec web python manage.py migrate --noinput

superuser:
	docker-compose exec web python manage.py createsuperuser

load_initial_data:
	docker-compose exec web python manage.py generate_projects

test:
	docker-compose exec web python3 manage.py test --settings=projement.setting_test

loctest:
	python3 manage.py test --settings=projement.setting_test