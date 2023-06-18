# calendar_manager_django
#TODO: Nice, I need to keep track of what I want to do with this project and everyday contribute, even if small
#TODO: Check all CRUDs
#TODO: User registration, email, password forgot, etc.
#TODO: User sessions
Can CRUD Events, Tasks, and Notes
Tasks are tied to events
User creations and user sessions
Testing

django-admin startproject mysite - creates new project
python3 manage.py runserver - run server at  http://127.0.0.1:8000/

python3 manage.py runserver 8080 - change port

python manage.py runserver 0.0.0.0:8000 - change port

As long as your tests are properly isolated, you can run them in parallel to gain a speed up on multi-core hardware. See test --parallel.

python3 manage.py migrate - updates changes to database
python3 manage.py makemigrations NAMEOFAPP - updates changes to database

python3 manage.py sqlmigrate nameofapp 00XXX - number of edit

python3 manage.py shell - SQL command line to objects

python3 manage.py createsuperuser