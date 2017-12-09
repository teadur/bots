import requests

def getCryptoPrice(currency):
    #currency = "LTC"
    result = "Damn APIs"
    url = "https://min-api.cryptocompare.com/data/price?fsym=" + currency + "&tsyms=EUR"

    r = requests.get(url)

    if r.status_code == 200:
        result = currency + " price: " + str(r.json().get('EUR', "Not found, moron")) + " EUR"
    return result