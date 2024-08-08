# Flask API and Postgres Container Setup
### This task is for week three and it is to set up both API and Postgres database containers with Docker Compose

## Expectations:
- API and its dependent services should be run using docker-compose.
- Makefile should have the following targets.
    - To start DB container.
    - To run DB DML migrations.
    - To build REST API docker image.
    - To run REST API docker container.   
- README.md file should be updated with instructions
    - To add pre-requisites for any existing tools that must already be installed (e.g., docker, make, etc
    - To run different make targets and the order of execution.
- When we run the make target to start the REST API docker container,
    - It should first start the DB and run DB DML migrations.
    - (Good to have) You can even include checks to see if the DB is already running and DB migrations are already applied.
    - Later it should invoke the docker compose command to start the API docker container.


## Prerequisites

- Linux OS
- Docker compose

## Run Docker compose 

```bash
docker-compose up --build 
```