## CRUD REST API
### This task is for week one and it is to dockerise the API using multistage Dockerfile

### Expectations:
- API should be run using the docker image.
- Dockerfile should have different stages to build and run the API.
- We should be able to inject environment variables while running the docker container at runtime.
- README.md should be updated with proper instructions to build the image and run the docker container.
- Similarly appropriate make targets should be added in the Makefile.
- The docker image should be properly tagged using semver tagging, use of latest tag is heavily discouraged.
- Appropriate measures should be taken to reduce docker image size. We want our images to have a small size 