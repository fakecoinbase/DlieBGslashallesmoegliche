import requests

while True:
    print("New Input:")
    key = input()
    value = input()
    print(" ")
    requests.get("http://192.168.0.3:8080/set?"+key+"="+value)
