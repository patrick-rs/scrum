# scrum
A personal project written in Python to track sprints and tasks.

## Database
The database is Postgres. Use the `create_tables.sql` to create a database user and tables. If you wish to change the connection details the following environment variables are checked for:
* `POSTGRES_SCRUM_ADMIN_PASSWORD` (default 'password') 
* `POSTGRES_SCRUM_HOST` (default 'localhost')
* `POSTGRES_SCRUM_PORT` (default '5432')

## Setup and Running
To run the program, first create a virtual environment in the projects folder:

`python -m venv venv`

Then activate the virtual envrionment:

`source venv/bin/activate`

Install dependancies:

`pip install -r requirements.txt`

Then start the server:

`python main.py`

## Run tests

Tests are written in Postman and are exported to the `scrum.postman_collection.json` file.
