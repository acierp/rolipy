import requests
from rpi import RPI

# will return catalog value as a dictionary but will give an extremely slow response as the limiteds catalog consists of over 400 items

itemdata = []

catalog = RPI.getlimitedsCatalog(format='id')

print(RPI.getitemAttributes(catalog))
