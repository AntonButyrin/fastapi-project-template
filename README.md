## Template for fastapi project
#### The template is created and adapted for my convenience
- Python version 3.9;
- Poetry is used to manage dependencies;
- The out-of-the-box database is used by postgres;
- How orm is used by sqlalchemy;
- The whole project is packaged in docker;
- Docker-compose is used for deployment;
- Alembic is used to work with migrations;
- The template is created for asynchronous use;
-------------
### Requirements versions
| Package | Version |
| :------------:|:---------------:|
| Python | 3.9 |
| Fastapi | 0.95.1 |
| Sqlalchemy | 2.0.13 |
| Poetry | 1.4.2 |
| Asyncpg | 0.27.0 |
| Alembic | 1.10.3 |
-------------
### Project structure
+ migrations/ <- *alembic default migrations*
+ src/ <- *main folder with services*
	+ core/ <- *folder with basic settings*
		+ config.py <- *Configs taken from .env and processed  pydantic*
		+ database.py <- *creating a database*
		+ exceptions.py <- *all possible exceptions used in the project are recorded in the dataclass format*
		+ models.py <- *basic models for inheritance#
		+ responses.py <- *all possible text responses used in the project are recorded in the dataclass format*
	+ main.py <- *main file fastapi*
+ .env <- * you create this file for env variables*
+ .gitignore
+ docker-compose.yml
+ Dockerfile
+ pyproject.toml
+ README.md
+ alembic.ini
-------------
### Install and usage (without docker-compose)
1) install poetry 1.4.2 version
`pip install poetry=1.4.2`
2) install poetry requirements
`poetry install`
3) create postgres database
4) create .env file in project for env variables:
+ migrations/
+ src/
	+ core/
	+ main.py 
+ .env  <- **create .env there**
+ .gitignore
+ docker-compose.yml
+ Dockerfile
+ pyproject.toml
+ README.md
+ alembic.ini
5) upgrade basic migrates:
`poetry run alembic upgrade head`
6) run application:
`poetry run uvicorn src.main:app --reload`
7) check success run on http://localhost:8000/ping, result : {"ping":"pong!"}

-------------
### Install and usage (with docker-compose)
1) create .env file in project for env variables:
+ migrations/
+ src/
	+ core/
	+ main.py 
+ .env  <- **create .env there**
+ .gitignore
+ docker-compose.yml
+ Dockerfile
+ pyproject.toml
+ README.md
+ alembic.ini
2) collecting an image:
`docker-compose build`
3) run container:
`docker-compose up`
4) check success run on http://localhost:8000/ping, result : {"ping":"pong!"}
