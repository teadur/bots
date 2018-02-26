import requests

def getCryptoPrice(currency):
    #currency = "LTC"
    result = "Damn APIs"
    url = "https://min-api.cryptocompare.com/data/price?fsym=" + currency + "&tsyms=EUR"

    r = requests.get(url)

    if r.status_code == 200:
        result = str(r.json().get('EUR', ""))
    if result == "":
        result = "Not found, moron"
    else:
        result = currency + " price: " + result + " EUR"
    return result