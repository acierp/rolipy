import requests
from rpi import RPI

items = [1029025, 1365767]

for item in items:
    print(RPI.idtoName(item) + '\'s value is ' + str(RPI.getValue(item)))