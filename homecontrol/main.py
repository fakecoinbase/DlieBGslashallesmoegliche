import threading, http.server, socketserver
import RPi.GPIO as GPIO
from http.server import HTTPServer, BaseHTTPRequestHandler
from collections import defaultdict
from time import sleep

global values

class Values:
    def __init__(self):
        self.values = defaultdict(lambda : "0")

    def set(self, key, value):
        self.values[str(key)]=str(value)

    def get(self, key):
        return self.values[str(key)]
        
    def switch(self, key):
        if values.get(key) is "0":
            values.set(key, "1")
            return
        if values.get(key) is "1":
            values.set(key, "0")

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()

        if "/get" in self.path:
            self.wfile.write(bytes( str(dict(values.values)) , encoding="utf8"))

        if "/json" in self.path:
            self.wfile.write(bytes( str(dict(values.values)).replace("'", '"') , encoding="utf8"))

        if "/set" in self.path:
            for part in self.path.split('?')[1].split('&'):
                values.set(part.split('=')[0], part.split('=')[1])

class Server:
    def __init__(self):
        httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
        httpd.serve_forever()

class Inputs:
    def __init__(self):
        self.setupInputs()
        while True:
            self.getInputs()
            sleep(0.01)
           
    def setupInputs(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)        

    def getInputs(self):
        if GPIO.input(4) == GPIO.HIGH:
            values.switch(1)
            while GPIO.input(4) == GPIO.HIGH:
                sleep(0.05)

class Outputs:
    def __init__(self):
        self.setupOutputs()
        while True:
            self.setOutputs()
            sleep(0.01)

    def setupOutputs(self):
        GPIO.setup(15, GPIO.OUT)

    def setOutputs(self):
        self.set(15, values.get(1))
        
    def set(self, gpio, value):
        if value is "0":
	        GPIO.output(gpio, GPIO.HIGH)
        if value is "1":
            GPIO.output(gpio, GPIO.LOW)

values = Values()

server = threading.Thread(target=Server)
server.daemon = True
server.start()

inputs = threading.Thread(target=Inputs)
inputs.daemon = True
inputs.start()

outputs = threading.Thread(target=Outputs)
outputs.daemon = True
outputs.start()


values.set(1, "1")


while True:
    print(dict(values.values))
    sleep(2)
