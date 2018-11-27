# Britecore Test project
[Description]

## Requirements
* Python 3

## Setup
* clone Repository containing the project `git clone git@github.com:Percayso-VS/serviceLocator.git`
* cd project `cd serviceLocator/src`
* set up mongo database
* Run `npm install` to install the needed node js packages.
* Setup Environment variables (check the .env.sample to see the environment variables needed).

## How to run
Run this command to run the application `npm start` and you can also use [pm2](https://github.com/Unitech/pm2) or other production process manager for Node.js such as [Forever](https://github.com/foreverjs/forever) and [Strong PM](https://github.com/strongloop/strong-pm) (check their documentation for usage).

## Running the test
From the commandline run the following commands

* cd  `cd serviceLocator/src`
* then run `npm test`

![Running Test](https://github.com/Percayso-VS/serviceLocator/blob/SERVICELOCATOR-10/documentation/screenshots/passing_tests.png?raw=true)

## Documentation

## Sample Environment Variables
* PORT = 3000
* NODE_ENV = 'development'
* DBURL='mongodb://localhost/development'
* MAPBOX_CLIENT_KEY=pk.YBido7dF89FldmMwcmYxMzBwZXI3d3BoY3htIndd.JMtVIIHI5BF6_fyQP8A
* ATM_API_URL=http://website.com/atmapi

#### Note: the values of the environment variables are dummy values.


![Atmbankbot running with outputResult set to true](https://github.com/Percayso-VS/serviceLocator/blob/SERVICELOCATOR-10/documentation/screenshots/atmbankbot.jpg?raw=true)

## Running the test



## Contributors
[Irale Usman](https://github.com/superirale)
