# Britecore Test project
[Description]

## Requirements
* Python 3.7.1
* Flask 1.0.2
* MySQL 5.7.14
* JQuery 3.3.1

#### Note: A complete list of dependencies can be found in requirements.txt


## Setup
* set up MYSQL database
* clone Repository containing the project `git@github.com:superirale/britecore-test.git`
* cd project `cd britecore-test`
* create a `.env` file from a sample `.env.sample` file and update the necessary variables
* create a virtual environment `python -m venv britecore`
* Initialize the virtual environment `. britecore/bin/activate`
* Run `pip install -r requirements.txt` to install the project dependencies.

## How to run
Execute the following commands to run the app locally:

* `export FLASK_ENV=development`
* `export FLASK_APP="run.py"`
*  `flask run`

You can also run the app using [gunicorn](https://gunicorn.org/) and [uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/) (check their documentation for usage).

## Running the test
From the commandline run the following commands

* cd  `cd britecore-test`
* Initialize the virtual environment if it is not already initialized `. britecore/bin/activate`
* then run `python app-test.py`

![Running Test](https://github.com/superirale/bitecore-test/blob/master/app/static/images/tests.png?raw=true)


## Sample Environment Variables
* APP_ENV=development
* SECRET_KEY=ab4fed44eef
* DEBUG=True
* DATABASE_URI=mysql+mysqlconnector://root:dummy@localhost/britecore
* DATABASE_URI_TEST=mysql+mysqlconnector://root:dummy@localhost/britecore_test

#### Note: the values of the environment variables are dummy values.



## Contributors
[Irale Usman](https://github.com/superirale)
