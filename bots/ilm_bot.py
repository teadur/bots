from telegram_backend import telegram_bot
from discord_backend import discord_bot
import lxml.etree as ET
import urllib.request, sys

def get_xml():
    req = urllib.request.Request(
    'http://www.ilmateenistus.ee/ilma_andmed/xml/observations.php',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
    )
    with urllib.request.urlopen(req) as response:
        string = response.read()
    xml = None
    parser = ET.XMLParser(remove_blank_text=True)
    try:
        xml = ET.ElementTree(ET.fromstring(string, parser)).getroot()
    except ET.XMLSyntaxError:
        return "Xml syntax error"
    return xml

def get_weather(place):
    weather = measurement = ""
    xml = get_xml()

    units = {
    "visibility":" km",
    "precipitations":" mm",
    "airpressure":" hPa",
    "relativehumidity":"%",
    "airtemperature":"°C",
    "winddirection":"°",
    "windspeed":" m/s",
    "windspeedmax":" m/s",
    "watertemperature":"°C",
    "waterlevel":"cm"
    }

    temp_comment = {
    -30: "kampsuni ilm",
    -20: "t-särgi ilm",
    -10: "lühikeste pükste ilm",
      0: "soe",
     10: "palav bljat",
     20: "kuradi palav bljät, ajuvedelik keeb",
     30: "põrgu"}

    wind_comment = {
    3:"kerged tupetuuled",
    6:"oh sa lits, kus puhub",
    9:"assa tuss, mis tuisk",
    12:"rape wind",
    15:"suema queef"}

    comment2tag = {
    "airtemperature":[temp_comment,"surm"],
    "windspeed":[wind_comment,"pardi peer"]}

    for n in xml.xpath("//name"):
        n.text = n.text.lower()
    weather_subtree = xml.xpath("//station[name[text()[contains(.,'" + place.lower() + "')]]]")[0]

    #print ET.tostring(weather_subtree, pretty_print = True)

    for child in weather_subtree.xpath("./*[not(name()='name') and not(name()='wmocode') and not(name()='longitude') and not(name()='latitude') and not(name()='waterlevel') and text()!='']"):
        if child.tag == "phenomenon":
            weather += child.text + "\n"
        elif child.tag in comment2tag:
            measurement +=  child.text + units[child.tag] + " "
            for limit in comment2tag[child.tag][0]:
                if float(child.text) < limit:
                    measurement += comment2tag[child.tag][0][limit] + "\n"
                    break
            else:
                measurement += comment2tag[child.tag][1] + "\n"
        else:
            weather += child.tag + " " + child.text + units.get(child.tag, "") + "\n"
    returnvalue = "Weather in " + place + ":\n" + measurement + weather
    return returnvalue

def get_placenames():
    xml = get_xml()
    placenames = []

    for p in xml.xpath("//station/name"):
        placenames.append(p.text)

    return " ".join(placenames)

class IlmBot(object):
    def create_response(self, args):
        response = []
        place = " ".join(args)
        if place == "":
            response.append(("string", get_weather("Tallinn")))
        elif place == "Marilyni kodu":
            response.append(("string", "lausmärt"))
        elif place == "tõde":
            response.append(("photo", 'ilm.jpg'))
        else:
            response.append(("string", get_weather(place)))
        if not response:
            response.append(("string", "Not found, try one of the following: \n" + get_placenames()))
        return response

class TelegramIlmBot(telegram_bot, IlmBot):
    def __init__(self):
        telegram_bot.__init__(self, "348367169:AAG4xGta0G35xRPn8nDQYngld12x-rxrCE4", "ilm", kick_on_empty=False)

class DiscordIlmBot(discord_bot, IlmBot):
    def __init__(self):
        discord_bot.__init__(self, "MzU1NTgwMDk1NTQ2NTIzNjQ5.DJO3-A.TKkY-GNO3kUTenjmnMfs6g-Dcsc", "ilm")

if sys.argv[1] == "telegram":
    TelegramIlmBot()
elif sys.argv[1] == "discord":
    DiscordIlmBot()
