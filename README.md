<p align="center">
  <a href="https://www.linkedin.com/in/zakharb/CeleryAPI">
  <img src="img/logo.png" alt="Lush Font " />
</p>

<p align="center">

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&pause=1000&color=75CC20&center=true&width=435&lines=Scrape+Links;Scrape+fast+with+Celery" alt="description" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0-green" height="20"/>
  <img src="https://img.shields.io/badge/python-3.11-green" height="20"/>
</p>


## :green_square: Getting Started

[CeleryAPI](https://github.com/zakharb/celeryapi) is the Service that parse website for Links and get additional infos from urls using Celery.  

### Requirements

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

### Installing

Clone the project

```
git clone git@github.com:zakharb/celeryapi.git
cd celeryapi
```

Start docker-compose

```
docker-compose up -d
```

## :green_square: Usage  


## :green_square: Configuration  
To solve problem with performance each Service run in container  
[Uvicorn]((https://www.uvicorn.org/)) work as ASGI server 
Main configuration is `docker-compose.yml`  

- every service located in separate directory `name-service`  
- use `Dockerfile` to change docker installation settings  
- folder `app` contain FastAPI application  
- all services connected to one piece in `docker-compose.yml`  
- example of service + DB containers (change `--workers XX` to increase multiprocessing)  

### Examples  
`Customer` service
```
services:
  web:
    build: ./backend
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    volumes:
      - ./backend/:/app/
    ports:
      - "8000:8000"
    env_file:
      - .env
    depends_on:
      - db
      - redis
      - worker

```


## :green_square: Deployment

Edit `Dockerfile` for each Microservice and deploy container

## :green_square: Versioning

Using [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/zakharb/celeryapi/tags). 

## :green_square: Authors

* **Zakhar Bengart** - *Initial work* - [Ze](https://github.com/zakharb)

See also the list of [contributors](https://github.com/zakharb/celeryapi/contributors) who participated in this project.

## :green_square: License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation - see the [LICENSE](LICENSE) file for details
