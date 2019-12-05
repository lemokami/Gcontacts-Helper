import base64
import requests

def imgmaker(url):
    enstring=''
    image = requests.get(url)
    enstring = str(base64.b64encode(image.content),"utf-8")
    return enstring