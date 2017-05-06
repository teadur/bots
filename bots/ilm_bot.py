from bot_backend import bot
import lxml.etree as ET
import urllib.request

def get_xml():
    with urllib.request.urlopen('http://www.ilmateenistus.ee/ilma_andmed/xml/observations.php') as response:
        string = response.read()
    xml = None
    parser = ET.XMLParser(remove_blank_text=True)
    try:
        xml = ET.ElementTree(ET.fromstring(string, parser)).getroot()
    except ET.XMLSyntaxError:
        return "Xml syntax error"
    return xml

def get_weather(place):
    weather = ""
    returnvalue = None
    xml = get_xml()

    units = {
    "visibility":" km",
    "precipitations":" mm",
    "airpressure":" hPa",
    "relativehumidity":"%",
    "airtemperature":"°C",
    "winddirection":"°",
    "windspeed":" m/s",
    "windspeedmax":" m/s"
    }

    for n in xml.xpath("//name"):
        n.text = n.text.lower()
    try:
        weather_subtree = xml.xpath("//station[name[text()[contains(.,'" + place.lower() + "')]]]")[0]

        #print ET.tostring(weather_subtree, pretty_print = True)
        for child in weather_subtree.xpath("./*[not(name()='name') and not(name()='wmocode') and text()!='']"):
            if child.tag == "phenomenon":
                weather += child.text + "\n"
            else:
                weather += child.tag + " " + child.text + units[child.tag] + "\n"
        returnvalue = "Weather in " + place + ":\n" + weather
    except:
        returnvalue = None
    return returnvalue

def get_placenames():
    xml = get_xml()
    placenames = []

    for p in xml.xpath("//station/name"):
        placenames.append(p.text)

    return " ".join(placenames)

class IlmBot(bot):
    def send_response(self, bot, update, args):
        print ("send_response")
        place = " ".join(args)
        if place == "":
            response = get_weather("Tallinn")
        elif place == "Marilyni kodu":
            response = "lausmärt"
        else:
            response = get_weather(place)
        if not response:
            response = "Not found, try one of the following: \n" + get_placenames()
        bot.sendMessage(chat_id=update.message.chat_id, text=response)

token = "348367169:AAG4xGta0G35xRPn8nDQYngld12x-rxrCE4"
IlmBot(token, None, None,"ilm")