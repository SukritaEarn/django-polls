# Django Polls Application

by Sukrita Kittipitayakorn.

## Features

This project is consist of two sites.

    1. An admin site that you can add, change, and delete your questions and choices.

    2. A polls site that shows your questions and choices, after you add them in the admin site.

## Requirements

The application requires python add-on modules as in [requirements.txt](requirements.txt)

## Built With

This project uses Django and Django tutorial app to develop and get several concept.

* [Tutorial 1](https://docs.djangoproject.com/en/2.2/intro/tutorial01/)
    - Create Project
    - Run development server
    - Create the Polls app
    - Write simplest "views" for the site
* [Tutorial 2](https://docs.djangoproject.com/en/2.2/intro/tutorial02/)
    - Setup database
    - Create model (database layout)
    - Create and Manage database schema
    - Create and Manage a Python database-access API
    - Genate an admin site
* [Tutorial 3](https://docs.djangoproject.com/en/2.2/intro/tutorial03/)
    - Create public interface(views)
    - Raise a 404 error
    - Use the template system
    - Namespace URL name for polls
* [Tutorial 4](https://docs.djangoproject.com/en/2.2/intro/tutorial04/)
    - Write simple form processing
    - Cut down our code
* [Tutorial 5](https://docs.djangoproject.com/en/2.2/intro/tutorial05/)
    - Create some automated testing
    - Fix some bugs

## How to Run

1. Clone the repository

        $ git clone https://github.com/SukritaEarn/django-polls

2. Change directory to django-polls
        
        $ cd /some/directory/django-polls

3. Install requirements
        
        $ pip3 install -r requirements.txt

4. Database migrations

        $ python3 manage.py migrate

5. Run server

        $ python3 manage.py runserver

6. In web browser open this link
        
        http://127.0.0.1:8000/

    Note: You will see There's no polls avaibles. You can add you own questions and choices by creating an admin user.

7. Create an admin user

        $ python manage.py createsuperuser

8. Enter your desired username, email address and password 

        Username: admin

        Email address: admin@example.com

        Password: **********
        Password (again): *********
        Superuser created successfully.

9. After finish creating an admin user, run server again. Now, go to this link
        
        http://127.0.0.1:8000/admin/    