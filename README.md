# Flask API Docker Setup
### This task is for week two and it is to dockerise the API using Dockerfile

## Expectations:
- API should be run using the docker image.
- Dockerfile should have different stages to build and run the API.
- We should be able to inject environment variables while running the docker container at runtime.
- README.md should be updated with proper instructions to build the image and run the docker container.
- Similarly appropriate make targets should be added in the Makefile.
- The docker image should be properly tagged using semver tagging, use of latest tag is heavily discouraged.
- Appropriate measures should be taken to reduce docker image size. We want our images to have a small size   



## Prerequisites

- Docker

## Build Docker Image

To build the Docker image, run:

```bash
docker build -t royalteegee/student-record-api:1.0 .    
```

## Run Docker Image

To run the Docker image, pass the Database URI as an environment variable and run:

```bash
docker run -d -p 80:5000 -e DB_URI=sqlite:///studentrecords.db --name api royalteegee/student-record-api:1.0  
```
