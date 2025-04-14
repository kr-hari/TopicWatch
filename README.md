# TopicWatch

## Objectives
Identify the latest trends/ issues/ topics related to ones interest.

## Features
- Reddit based trend identification
- User data management

## Contributors
Harikrishnan Raghukumar (harikrishnankr16@gmail.com), Sneha Mishra(mishra.sneha4321@gmail.com)

## Requirements
- Install docker
- Install MongoDB compass from https://www.mongodb.com/try/download/compass (for GUI access to MongoDB)

# Dev ReadMe

## Docker Related
- run `docker-compose up -d` (to run the containers)
- run `docker compose down -v` (to remove the containers and the data as well)
- run `docker compose up --build` (to rebuild with all the details)

## Python scripts
- To run INGESTOR : `uvicorn apps.ingestor.main:app --reload --port 8080`
- To run user_service: `python3 -m uvicorn apps.user_service.main:app --reload`

## API related 
- To see swagger and test out API: http://127.0.0.1:8080/docs

