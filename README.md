Use the following command to install Django

```
pip install django
```

Use the following command to start the server

```
python manage.py runserver
```
The Server should run on port no 8000. Use the following url to access the asgard webpage:
```
http://localhost:8000/
```
The data in the database needs to be added manually using the django's default admin page

```
http://localhost:8000/admin/
```

To be able to access the admin page just use the following command to create a new super user

```
python manage.py createsuperuser
```

The data is stored in SQLLite database locally
