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
    "windspeedmax":" m/s"
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
    try:
        weather_subtree = xml.xpath("//station[name[text()[contains(.,'" + place.lower() + "')]]]")[0]

        #print ET.tostring(weather_subtree, pretty_print = True)
        for child in weather_subtree.xpath("./*[not(name()='name') and not(name()='wmocode') and text()!='']"):
            if child.tag == "phenomenon":
                weather += child.text + "\n"
            elif child.tag in comment2tag:
                measurement =  child.text + units[child.tag] + " "
                for limit in comment2tag[child.tag][0]:
                    if float(child.text) < limit:
                        measurement += comment2tag[child.tag][0][limit] + "\n"
                        break
                else:
                    measurement += comment2tag[child.tag][1] + "\n"
            else:
                weather += child.tag + " " + child.text + units[child.tag] + "\n"
        returnvalue = "Weather in " + place + ":\n" + measurement + weather
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
        place = " ".join(args)
        if place == "":
            response = get_weather("Tallinn")
        elif place == "Marilyni kodu":
            response = "lausmärt"
        elif place == "tõde":
            bot.send_photo(chat_id=update.message.chat_id, photo=open('ilm.jpg', 'rb'))
            response = "TRUTH"
        else:
            response = get_weather(place)
        if not response:
            response = "Not found, try one of the following: \n" + get_placenames()
        bot.sendMessage(chat_id=update.message.chat_id, text=response)

token = "348367169:AAG4xGta0G35xRPn8nDQYngld12x-rxrCE4"
IlmBot(token, None, "ilm")
