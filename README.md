# Juego de Tornos Characters Microservice
Microservice that exposes an API to perform CRUD operations over the Characters Database

## Requirements
Having [Docker](https://docs.docker.com/install/) and [Docker Compose](https://docs.docker.com/compose/install/) installed.

## Installation

1. Build and run the project: `docker-compose up --build -d`
2. Init database:

   `docker-compose exec characters_api flask db init`
   
   `docker-compose exec characters_api flask db migrate`
   
   `docker-compose exec characters_api flask db upgrade`
   
After these steps you should be able to access a swagger ui through the url http://0.0.0.0:8082/api/ui

## Optional

The database is empty, but you can fill it with some examples running:

`docker-compose exec characters_api python utils/populate_database.py`
