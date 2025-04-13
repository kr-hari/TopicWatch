# TopicWatch

## Objectives
Identify the latest trends/ issues/ topics related to ones interest.

## Features
- Reddit based trend identification
- User data management

## Contributors
Harikrishnan Raghukumar (harikrishnankr16@gmail.com), Sneha Mishra(sneha.mishra4321@gmail.com)

## Requirements
- Install docker
- Install MongoDB compass from https://www.mongodb.com/try/download/compass (for GUI access to MongoDB)

# Dev ReadMe

- run `docker-compose up -d`
- To run INGESTOR : `uvicorn apps.ingestor.main:app --reload --port 8080`


- To see swagger and test out API: http://127.0.0.1:8080/docs