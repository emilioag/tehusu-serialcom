import serial
import re
import time
import requests
from requests.auth import HTTPBasicAuth
from configs import USERNAME, PASSWORD, HOST



if __name__ == '__main__':
    s = serial.Serial('/dev/tty.usbmodem1411', 9600)
    regex = re.compile("b\'Humedad\srelativa:\s(\d\d?)\s\%\\\\tTemperatura:\s(\d\d?)")
    max_temp, min_temp, max_hume, min_hume = '', '', '', ''
    while True:
        mybytes = s.readline()
        text = str(mybytes)
        r = regex.search(text)
        if r:
            data = {
                "instant": time.time(),
                "temperature": r.group(2),
                "humidity": r.group(1)
            }
            requests.post(url=HOST, auth=HTTPBasicAuth(USERNAME, PASSWORD), json=data)
