import requests, json
class RPI:
    def getValue(assetid, proxy=None):
        if proxy == None:
            itemdetails = requests.get("https://www.rolimons.com/itemapi/itemdetails")
            print(itemdetails.text)
            #for item in itemdetails.json():
        else: 
            if proxy.startswith("https://"):
                itemdetails = requests.get("https://www.rolimons.com/itemapi/itemdetails", proxies = {"https": proxy})
            elif proxy.startswith("http://") or proxy.startswith('socks5://'):
                itemdetails = requests.get("https://www.rolimons.com/itemapi/itemdetails", proxies = {"http": proxy})
            else:
                if "://" in proxy:
                    proxytype = proxy.split('://')[0]
                    raise ConnectionError("Proxy format " + proxytype + " is not supported")
                else:
                    raise ConnectionError("Proxy format is unknown or unsupported")

value = RPI.getValue('1111', proxy='http://hihihi')
