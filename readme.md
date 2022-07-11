Shortener

#### Service helps you to short links like:
    
     http://example.com/longurl ->  http://mydomain/9jO13C

### HOW TO RUN:

*First you have to provide host http and django secret key in .env file*

      SECRET_KEY=example_key
      HOST_HTTP=http://127.0.0.1:8000/

*Then you just need to run:*
    
    1. pip install -r requirements.txt
    2. python manage.py makemigrations
    3. python manage.py migrate
    4. python manage.py createsuperuser (optional)
    5. python manage.py runserver
    

*USED PACKAGES AND MODULES:*

- Python 3.10
- Django 3.2.9
- Django ORM
- HTML
- Jinja2
- Pathlib
- Hashlib
- os
- dotenv
- flake8

(MySQL task solution contained in 'my_sql_test_task_solution.sql' file)
