import requests, json, string
class RPI:
    def getlimitedsCatalog(format=None):
        total = []
        itemdetails = requests.get("https://www.rolimons.com/itemapi/itemdetails")
        if format == 'id' or format == None:
            for itemobj in itemdetails.json()['items']:
                total.append(itemobj)
            return total
        elif format == 'name':
            for itemobj in itemdetails.json()['items']:
                total.append(itemdetails.json()['items'][str(itemobj)][0])
            return total
            
    def getValue(item, proxy=None): 
        itemdetails = requests.get("https://www.rolimons.com/itemapi/itemdetails")
        itemcheck = itemdetails.json()['items'][str(item)][3]

        if str(itemcheck) != "-1":
            return itemdetails.json()['items'][str(item)][3]
        else:
            return itemdetails.json()['items'][str(item)][2]

    def idtoName(item):
        return requests.get("https://www.rolimons.com/itemapi/itemdetails").json()['items'][str(item)][0]
    
    def getitemAttributes(items):
        if not isinstance(items, list):
            demandcheck = {-1: None, 0: 'terrible', 1: 'low', 2: 'normal', 3: 'high', 4: 'amazing'}
            trends = {-1: None, 0: 'lowering', 1: 'unstable', 2: 'stable', 3: 'raising', 4: 'fluctuating'}
            boolcheck = {-1: False, 1: True}
            rtn = {}
            itemdetails = requests.get("https://www.rolimons.com/itemapi/itemdetails")

            if str(itemdetails.json()['items'][str(items)][3]) == '-1':
                val = None
            else:
                val = itemdetails.json()['items'][str(items)][3]
            if str(itemdetails.json()['items'][str(items)][4]) == '-1':
                defaultval = None
            else:
                defaultval = itemdetails.json()['items'][str(items)][4]
            if int(itemdetails.json()['items'][str(items)][6]) == 4:
                trend = 'fluctuating'
            rtn[items] = {'name': itemdetails.json()['items'][str(items)][0], 'acronym': itemdetails.json()['items'][str(items)][1], 'rap': itemdetails.json()['items'][str(items)][2], 'value': val, 'default_value': defaultval, 'demand': demandcheck[itemdetails.json()['items'][str(items)][5]], 'trend': trends[itemdetails.json()['items'][str(items)][6]], 'projected': boolcheck[itemdetails.json()['items'][str(items)][7]], 'hyped': boolcheck[itemdetails.json()['items'][str(items)][8]], 'rare': boolcheck[itemdetails.json()['items'][str(items)][9]]}
            return rtn[items]
        elif isinstance(items, list):
            demandcheck = {-1: None, 0: 'terrible', 1: 'low', 2: 'normal', 3: 'high', 4: 'amazing'}
            trends = {-1: None, 0: 'lowering', 1: 'unstable', 2: 'stable', 3: 'raising', 4: 'fluctuating'}
            boolcheck = {-1: False, 1: True}
            rtn = {}

            itemdetails = requests.get("https://www.rolimons.com/itemapi/itemdetails")
            for itemcheck in items:
                if str(itemdetails.json()['items'][str(itemcheck)][3]) == '-1':
                    val = None
                else:
                    val = itemdetails.json()['items'][str(itemcheck)][3]
                if str(itemdetails.json()['items'][str(itemcheck)][4]) == '-1':
                    defaultval = None
                else:
                    defaultval = itemdetails.json()['items'][str(itemcheck)][4]
                rtn[itemcheck] = {'name': itemdetails.json()['items'][str(itemcheck)][0], 'acronym': itemdetails.json()['items'][str(itemcheck)][1], 'rap': itemdetails.json()['items'][str(itemcheck)][2], 'value': val, 'default_value': defaultval, 'demand': demandcheck[itemdetails.json()['items'][str(itemcheck)][5]], 'trend': trends[itemdetails.json()['items'][str(itemcheck)][6]], 'projected': boolcheck[itemdetails.json()['items'][str(itemcheck)][7]], 'hyped': boolcheck[itemdetails.json()['items'][str(itemcheck)][8]], 'rare': boolcheck[itemdetails.json()['items'][str(itemcheck)][9]]}
            return rtn

    def getcatalogCount():
        return requests.get('https://www.rolimons.com/itemapi/itemdetails').json()['item_count']

itemdetails = RPI.getitemAttributes(21070012)

print(itemdetails['name'], itemdetails['acronym'], itemdetails['value'], itemdetails['demand'], itemdetails['trend'])