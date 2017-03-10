# A Web Server Powered by a Snake, a Bottle and (maybe) a Container

A simple Python "hello world" server that can be run in Docker using Bottle.

Bottle is a fast, simple and lightweight micro web-framework for Python.

The examples are taken from the Bottle tutorials at:

* https://bottlepy.org/docs/dev/ - Hello World
* https://bottlepy.org/docs/dev/stpl.html - Bottle Templates
* https://bottlepy.org/docs/dev/tutorial_app.html - TODO List Application


### Quick Start - Run Stand Alone Server
This image exists in the index.docker.io registry already, so you can run it with:
```
$ pip install -r requirements.txt
$ ./sqlCreate.py
$ ./server.py
$ curl http://0.0.0.0:8080/project/welcome/world
$ <h1>Hello world!</h1>
```

This will:

* Create an SQL database called dependencyList.db
* Start up a web server at http://0.0.0.0:8080/
* Verify the server over HTTP and return a simple Hello world response.


#### Summary of Files

The server code is fully contained in `server.py` and the only dependency is on Bottle (which is specified in requirements.txt)

The `/views` directory contains some Bottle templates to help with the format of the output of the REST calls (HTML + Python)

`sqlCreate.py` needs to be just run once in order to create the initial db for the dependency list.

`Dockerfile` contains everything needed to run the server in a docker container.

#### Simple End Points
The server has a number of simple end points built in that can be called:

* http://0.0.0.0:8080/project/celebrate/day/your%20name - celebrate an engineer!
* http://0.0.0.0:8080/project/celebrate/v2/day/your%20name - celebrate an engineer using a bottle template
* http://0.0.0.0:8080/project/json/example - return some example JSON

#### More Complex End Points
It also has a more complex example - a project dependency list backed by an SQL db

* http://0.0.0.0:8080/dependency - list all of the open dependencies
* http://0.0.0.0:8080/dependency/json/1 - show dependency at index 1 in JSON format
* http://0.0.0.0:8080/dependency/json/all - show all dependencies in JSON format
* http://0.0.0.0:8080/dependency/new - add a new dependency

This simple dependency list could be easily improved with edit and remove functionality if
you want to try your hand at bottle.

### Running the Server in Docker

First build the docker image from the Dockerfile:

```
$ docker build -t you/your_tag_name /PATH/TO/THIS/REPOSITORY
```

Then run the newly created image as a container:
```
$ docker run -d -p 8080 you/your_tag_name
```

This will map port 8080, which the server is listening on, to a dynamically allocated port on the host. You can see which port by running `docker ps`:
```
$ docker ps
CONTAINER ID        IMAGE                                    COMMAND                CREATED             STATUS              PORTS                     NAMES
e9b36d702141        you/your_tag_name:latest   /usr/bin/python /hom   3 seconds ago       Up 2 seconds        0.0.0.0:49173->8080/tcp   kickass_archimedes
```
This shows that port 8080 on the container is mapped to port 49173 on the host. Thus, assuming `curl` is installed (if not, run `sudo apt-get install curl` first), you can do:
```
$ curl localhost:49173/project/welcome/World
Hello World!
```

To see the output from the container (i.e. the bottle web server logs) run:
```
docker attach kickass_archimedes
```

To login to the container's shell prompt run:
```
docker exec -i -t kickass_archimedes sh
```

The docker approach is taken (in part) from https://github.com/joshuaconner/hello-world-docker-bottle
