import paho.mqtt.client as mqtt
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

# Callback cuando el cliente se conecta al broker MQTT
def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Conectado al broker con código {rc}")
    client.subscribe("test/topic")  # Nos suscribimos al tema "test/topic"

# Callback cuando se recibe un mensaje en el tema MQTT
def on_message(client, userdata, msg):
    print(f"Mensaje recibido en el tema {msg.topic}: {msg.payload.decode()}")
    # Emitimos el mensaje a través de SocketIO para que lo reciba el cliente
    socketio.emit('mqtt_message', {'message': msg.payload.decode()})

# Usamos MQTT 5.0 para evitar el warning de deprecación
webpage = mqtt.Client(protocol=mqtt.MQTTv5)  # Actualizamos el cliente para usar MQTTv5

# Asignamos las funciones de callback
webpage.on_connect = on_connect
webpage.on_message = on_message

# Nos conectamos al broker MQTT
webpage.connect("test.mosquitto.org", 1883, 60)

# Iniciamos el loop del cliente MQTT en un hilo para no bloquear el servidor Flask
webpage.loop_start()

@app.route('/')
def page():
    return render_template('page.html')  # Asegúrate de que este archivo esté en la carpeta templates

if __name__ == '__main__':
    print("Iniciando el servidor Flask...")
    socketio.run(app, host='0.0.0.0', port=3000)




