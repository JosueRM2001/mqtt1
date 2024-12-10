# MQTT
This is a project that was developed with Python in an MQTT architecture.

## Description
This project shows a page that allows us to enter a word or phrase that will return the phrase that was sent.
It is a simple program to show how a program works in the programming language with an architectural style.

## Technologies Used
**Contains the Following**
- Visual Studio Code (most current version)
- Docker
- MQTT
- flask
- flask-socketio
- paho-mqtt
- gevent
- gevent-websocket

## Development Requirements
- **Docker Desktop** (if you want to run it in a container)
- **Visual Studio code** (optional, but recommended)
- **MQTT**(required and recommended)
- **GitHub Desktop** (if you want to clone and use the project)

```bash
https://www.docker.com/products/docker-desktop/
```

- **Docker hub** (if you want to clone and use the project)

```bash
https://hub.docker.com/layers/erickjrm/programqtt/latest/images/sha256-732eef85a25bc2f69b0efae71806a9dddd8f61c8c72ec5ea721400660f75661e?context=repo
```

## Instructions to run the project
## Steps to run
- **Step #1**
**Clone this repository**
If you have not yet cloned the repository, you can do so with the following link:

```bash
https://github.com/JosueRM2001/webhook1.git
```
- **Step #2**
**Build the Docker image**

Run the following command, which will generate the image:

```bash
docker pull erickjrm/programqtt:latest
```

**Step #3**
**Run the Docker container:**

Then run the following command, which generates the container and port.

```bash
docker run -d -p 3000:3000 --name mqtt erickjrm/programqtt:latest
```

**Step #4**

Open Docker Desktop to see if the image was built successfully and send it to run to view it.

**Step #5**

**Access the application**: If it is running, you can access the application by navigating to the

following url in your web browser:

```bash
http://localhost:3000
```
