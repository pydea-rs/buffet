pip3 install -r requirements.txt
python3 manage.py collectstatic
python3 manage.py makemigrations account food
python3 manage.py migarte
python3 manage.py runserver
