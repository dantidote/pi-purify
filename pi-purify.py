from gpiozero import DigitalOutputDevice
import flask
from flask import request
current = 1

dev = DigitalOutputDevice(4,active_high=False,initial_value=False)

app = flask.Flask(__name__)

@app.route('/',methods=['GET'])

def home():
    global current
    speed = request.args.get('speed')
    current = setSpeed(int(speed))
    return "ok"

def setSpeed(target):
    global current
    num=(target-current) % 4
    dev.blink(on_time=0.25,off_time=0.25,n=num,background=False)
    return target

app.run(host='0.0.0.0',port=8080)
