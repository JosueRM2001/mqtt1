import paho.mqtt.client as mqtt
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

def on_connect(client, userdata, flags, rc):
    print(f"Conectado al broker con código {rc}")
    client.subscribe("test/topic")   # Suscripción al tema

def on_message(client, userdata, msg):
    print(f"Mensaje recibido en el tema {msg.topic}: {msg.payload.decode()}")
    socketio.emit('mqtt_message', {'message': msg.payload.decode()})  # Emitir mensaje a través de SocketIO

webpage = mqtt.Client()

webpage.on_connect = on_connect
webpage.on_message = on_message

# Conectar al broker MQTT
webpage.connect("test.mosquitto.org", 1883, 60)

webpage.loop_start()  # Iniciar el loop para recibir mensajes MQTT

@app.route('/')
def page():
    return render_template('page.html')  # Renderizar el archivo HTML

if __name__ == '__main__':
    print("Iniciando el servidor Flask...")
    socketio.run(app, host='0.0.0.0', port=3000)  # Ejecutar Flask con SocketIO


