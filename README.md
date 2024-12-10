# MQTT
Este es un proyecto que fue desarrollado con Python en una arquitectura MQTT.

## Descripción
Este proyecto muestra una página que nos permite ingresar un palabra o frase que nos regresara la frase que se envio. 
Es un programa sencillo para mostrar cómo funciona un programa en el lenguaje de programación con un estilo de arquitectura.

## Tecnologías Utilizadas
**Contiene lo Siguiente**
- Visual Studio Code (version mas actual)
- Docker
- MQTT
- flask
- flask-socketio
- paho-mqtt
- gevent
- gevent-websocket

## Requerimientos para el Desarrollo
- **Docker Desktop** (si lo quieres correr en un contenedor)
- **Visual Studio code** (opcional, pero recomendado)
- **MQTT**(requerido y recomendado)
- **GitHub Desktop** (si quieres clonar y usar el proyecto)
  
  ```bash
  https://www.docker.com/products/docker-desktop/
  ```
  
- **Docker hub** (si quieres clonar y usar el proyecto)
  
  ```bash
  https://hub.docker.com/layers/erickjrm/programqtt/latest/images/sha256-732eef85a25bc2f69b0efae71806a9dddd8f61c8c72ec5ea721400660f75661e?context=repo
  ```

## Intruciciones para ejecutar el proyecto
## Pasos para ejecutar
- **Paso #1**
  **Clonar este repositorio**
Si aún no ha clonado el repositorio, puede hacerlo con el siguiente link:

 ```bash
https://github.com/JosueRM2001/webhook1.git
 ```
- **Paso #2**
  **Construya la imagen de Docker**

Ejecuta el siguiente comando, que generará la imagen:

```bash
docker pull erickjrm/programqtt:latest
```

**Paso #3**
**Ejecute el contenedor Docker:**

Luego ejecuta el siguiente comando, que genera el contenedor y el puerto.

```bash
docker run -d -p 3000:3000 --name mqtt erickjrm/programqtt:latest
```

**Paso #4**

Abre Docker Desktop para ver si la imagen se creó correctamente y envíala a ejecutar para verla.

**Paso #5**

**Accede a la aplicación**: Si está ejecutándose, puedes acceder a la aplicación navegando a la

siguiente url en tu navegador web:

```bash
http://localhost:3000
```
