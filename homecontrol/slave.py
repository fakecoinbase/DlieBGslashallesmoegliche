import threading, http.server, socketserver
import RPi.GPIO as GPIO
import requests
import ast
from collections import defaultdict
from time import sleep

global values

class Values:
    def __init__(self):
        self.values = defaultdict(lambda : "0")

    def set(self, key, value):
        updater = requests.get('http://192.168.0.3:8080/set?'+str(key)+"="+str(value))    
        
        self.values[str(key)]=str(value)

    def get(self, key):
        return self.values[str(key)]
        
    def switch(self, key):
        if values.get(key) is "0":
            values.set(key, "1")
            return
        if values.get(key) is "1":
            values.set(key, "0")

class Client:
    def __init__(self):
        while True:
            connection = requests.get("http://192.168.0.3:8080/get")
            values.values = ast.literal_eval(connection.text)    
            sleep(2)

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

client = threading.Thread(target=Client)
client.daemon = True
client.start()

inputs = threading.Thread(target=Inputs)
inputs.daemon = True
inputs.start()

outputs = threading.Thread(target=Outputs)
outputs.daemon = True
outputs.start()


values.set("s1", "1")


while True:
    print(dict(values.values))
    sleep(2)
