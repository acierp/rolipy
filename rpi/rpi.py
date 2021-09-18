import requests, json, string
class RPI:
    def getlimitedsCatalog(format=None, proxy=None):
        total = []

        if format == None:
            format = 'id'

        if proxy == None:
            itemdetails = requests.get("https://www.rolimons.com/itemapi/itemdetails")
            if format == 'id':
                for itemobj in itemdetails.json()['items']:
                    total.append(itemobj)
                return total
            elif format == 'name':
                for itemobj in itemdetails.json()['items']:
                    total.append(itemdetails.json()['items'][str(itemobj)][0])
                return total
        else: 
            if proxy.startswith("https://"):
                itemdetails = requests.get("https://www.rolimons.com/itemapi/itemdetails", proxies = {"https": proxy})
                if format == 'id':
                    for itemobj in itemdetails.json()['items']:
                        total.append(itemobj)
                    return total
                elif format == 'name':
                    for itemobj in itemdetails.json()['items']:
                        total.append(itemdetails.json()['items'][str(itemobj)][0])
                    return total
                pass
            elif proxy.startswith("http://") or proxy.startswith('socks5://'):
                itemdetails = requests.get("https://www.rolimons.com/itemapi/itemdetails", proxies = {"http": proxy})
                if format == 'id':
                    for itemobj in itemdetails.json()['items']:
                        total.append(itemobj)
                    return total
                elif format == 'name':
                    for itemobj in itemdetails.json()['items']:
                        total.append(itemdetails.json()['items'][str(itemobj)][0])
                    return total
            else:
                if "://" in proxy:
                    proxytype = proxy.split('://')[0]
                    raise ConnectionError("Proxy format " + proxytype + " is not supported")
                else:
                    raise ConnectionError("Proxy format is unknown or unsupported")
            

    def getValue(item, proxy=None):
        if not item.isdigit():
            pass
        if proxy == None:
            itemdetails = requests.get("https://www.rolimons.com/itemapi/itemdetails", proxies = {"https": proxy})
            itemcheck = itemdetails.json()['items'][str(item)][3]

            if str(itemcheck) != "-1":
                return itemdetails.json()['items'][str(item)][3]
            else:
                return itemdetails.json()['items'][str(item)][2]
        else: 
            if proxy.startswith("https://"):
                itemdetails = requests.get("https://www.rolimons.com/itemapi/itemdetails", proxies = {"https": proxy})
                itemcheck = itemdetails.json()['items'][str(item)][3]

                if str(itemcheck) != "-1":
                    return itemdetails.json()['items'][str(item)][3]
                else:
                    return itemdetails.json()['items'][str(item)][2]
            elif proxy.startswith("http://") or proxy.startswith('socks5://'):
                itemdetails = requests.get("https://www.rolimons.com/itemapi/itemdetails", proxies = {"http": proxy})
                itemcheck = itemdetails.json()['items'][str(item)][3]

                if str(itemcheck) != "-1":
                    return itemdetails.json()['items'][str(item)][3]
                else:
                    return itemdetails.json()['items'][str(item)][2]
            else:
                if "://" in proxy:
                    proxytype = proxy.split('://')[0]
                    raise ConnectionError("Proxy format " + proxytype + " is not supported")
                else:
                    raise ConnectionError("Proxy format is unknown or unsupported")
    def idtoName(item, proxy=None):
        if proxy == None:
            itemdetails = requests.get("https://www.rolimons.com/itemapi/itemdetails")
            return itemdetails.json()['items'][str(item)][0]
            #for item in itemdetails.json():
        else: 
            if proxy.startswith("https://"):
                itemdetails = requests.get("https://www.rolimons.com/itemapi/itemdetails", proxies = {"https": proxy})
                return itemdetails.json()['items'][str(item)][0]
            elif proxy.startswith("http://") or proxy.startswith('socks5://'):
                itemdetails = requests.get("https://www.rolimons.com/itemapi/itemdetails", proxies = {"http": proxy})
                return itemdetails.json()['items'][str(item)][0]
            else:
                if "://" in proxy:
                    proxytype = proxy.split('://')[0]
                    raise ConnectionError("Proxy format " + proxytype + " is not supported")
                else:
                    raise ConnectionError("Proxy format is unknown or unsupported")

print(RPI.getlimitedsCatalog(format='name'))