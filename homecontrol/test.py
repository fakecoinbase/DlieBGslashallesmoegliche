import requests
import time

while True:
    requests.get('http://192.168.0.3:8080/set?s1=0')
    time.sleep(1000)
    requests.get('http://192.168.0.3:8080/set?s1=1')
    time.sleep(1000)
