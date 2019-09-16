# Django Polls Application

by Sukrita Kittipitayakorn.

## Features

This project is consist of two sites.

    1. A site that lets people view polls and vote them.
    2. An admin site that you can add, change, and delete polls.

## Requirements

 The application requires
 * Python 3.6 or newer
 * Django 2.1.2 or newer
 * Python add-on modules as in [requirements.txt](requirements.txt)

## Installing

I use Django to create this poll application.
You can install Django from this [Install Guide](https://docs.djangoproject.com/en/2.2/intro/install/).

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
    In Terminal

    1. $ cd mysite

    2. $ python3 manage.py runserver

    3.1. If you want to go to admin site, go to this link http://127.0.0.1:8000/admin/

    3.2. If you want to go to polls site, use this link http://127.0.0.1:8000/polls/

    4.1. In the admin site, you can manage your questions and choices there.

    4.2. In the polls site, you will see two questions, click the questions and vote one of 
    the choices in there.
    
    5. You can see the result after you click vote.
    