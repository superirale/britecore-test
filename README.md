# Britecore Test project

I created this app as part of the britecore engineering coding challenge, the app allows users to submit feature requests and order them by priority.

## Project details
Build a web application that allows the user to create "feature requests".
A "feature request" is a request for a new feature that will be added onto an existing piece of software. Assume that the user is an employee at IWS who would be entering this information after having some correspondence with the client that is requesting the feature. The necessary fields are:

* Title: A short, descriptive name of the feature request.
* Description: A long description of the feature request.
* Client: A selection list of clients (use "Client A", "Client B", "Client C")
* Client Priority: A numbered priority according to the client (1...n). Client Priority numbers should not repeat for  the given client, so if a priority is set on a new feature as "1", then all other feature requests for that client should be reordered.
* Target Date: The date that the client is hoping to have the feature.
* Product Area: A selection list of product areas (use 'Policies', 'Billing', 'Claims', 'Reports')

## Requirements
* Python 3.7.1
* Flask 1.0.2
* MySQL 5.7.14
* JQuery 3.3.1

#### Note: A complete list of dependencies can be found in requirements.txt


## Setup
* Set up MYSQL database (create two database demo and test)
* Clone Repository containing the project `git@github.com:superirale/britecore-test.git`
* Navigate to the project directory `cd britecore-test`
* Create a `.env` file from a sample `.env.sample` file and update the necessary variables
* Create a virtual environment `python -m venv britecore`
* Initialize the virtual environment `source britecore/bin/activate`
* Execute command `pip install -r requirements.txt` to install the project dependencies.
* Run `export DATABASE_URI="mysql+mysqlconnector://[connection_string]"`
* Run `export DATABASE_URI_TEST="mysql+mysqlconnector://[connection_string]"`
* Run the migrations using `python manage.py db upgrade`

## How to run
Execute the following commands to run the app locally:

### Method 1
* Execute command `export FLASK_ENV="development"` to set flask environment
* Execute command `export FLASK_APP="run.py"` to set flask application entry point
* Execute Command `flask run` to launch the app

### Method 2
You can simply use gunicorn to run the app `gunicorn --bind 0.0.0.0:5000 run:app`, you can also run the app using [uwsgi](https://uwsgi-docs.readthedocs.io/en/latest/) (check their documentation for usage).

#### Note: The live demo can be found [here](http://217.69.6.212/) running on ubuntu 18.04 served using Gunicorn and Nginx.

## Running the test
From the commandline run the following commands

* Navigate to the project directory `cd britecore-test`
* Initialize the virtual environment if it is not already initialized `. britecore/bin/activate`
* Execute the following command `python app-test.py` to run the unit tests

![Running Test](https://raw.githubusercontent.com/superirale/britecore-test/master/app/static/images/tests.png)


## Sample Environment Variables
* APP_ENV=development
* SECRET_KEY=ab4fed44eef
* DEBUG=True
* DATABASE_URI=mysql+mysqlconnector://root:dummy@localhost/britecore
* DATABASE_URI_TEST=mysql+mysqlconnector://root:dummy@localhost/britecore_test

#### Note: the values of the environment variables are dummy values.



## Contributors
[Irale Usman](https://github.com/superirale)
