import random, requests, datetime, time, re, io, lxml.etree as ET, lxml.html as html

def strTimeProp(start, end, format, prop):
        """Get a time at a proportion of a range of two formatted times.
    
        start and end should be strings specifying times formated in the
        given format (strftime-style), giving an interval [start, end].
        prop specifies how a proportion of the interval to be taken after
        start.  The returned time will be in the specified format.
        """
    
        stime = time.mktime(time.strptime(start, format))
        etime = time.mktime(time.strptime(end, format))
    
        ptime = stime + prop * (etime - stime)
    
        return time.strftime(format, time.localtime(ptime))

def randomDate(start, end, prop):
        return strTimeProp(start, end, '%B-%d-%Y', prop)

def sendImage(token, path):
        url = "https://api.telegram.org/bot{}/sendPhoto".format(token);
        files = {'photo': open('/path/to/img.jpg', 'rb')}
        data = {'chat_id' : "YOUR_CHAT_ID"}
        r= requests.post(url, files=files, data=data)
        #print(r.status_code, r.reason, r.content)

def sendImageRemoteFile(token, img_url, chat_id):
        url = "https://api.telegram.org/bot{}/sendPhoto".format(token);
        remote_image = requests.get(img_url)
        photo = io.BytesIO(remote_image.content)
        photo.name = 'img.png'
        files = {'photo': photo}
        data = {'chat_id' : chat_id}
        r= requests.post(url, files=files, data=data)
        #print(r.status_code, r.reason, r.content)

def get_random_hagar_image():
        random_date = randomDate("january-7-1996", datetime.datetime.now().strftime("%B-%d-%Y"), random.random())
        url_to_dilbert_page = "http://hagarthehorrible.com/comics/%s/" % random_date
        response = requests.get(url_to_dilbert_page)
        first_half = response.text[response.text.find("https://safr.kingfeatures.com"):]
        data_image = first_half[:first_half.find('"')]
        return [data_image, random_date]

def get_random_ernie_image():
        random_date = randomDate("september-6-1998", datetime.datetime.now().strftime("%B-%d-%Y"), random.random())
        url_to_dilbert_page = "http://piranhaclubcomics.com/comics/%s/" % random_date
        response = requests.get(url_to_dilbert_page)
        first_half = response.text[response.text.find("https://safr.kingfeatures.com"):]
        data_image = first_half[:first_half.find('"')]
        return [data_image, random_date]

def get_random_xkcd_image():
        #insult_bot = "297812849:AAFGeKrSX3lyWv3m5XGiu3pr9G6wuLae1E8"
        #clicbait = "-1001071499716" 
        response = requests.get("http://c.xkcd.com/random/comic/")
        #print response.text
        page = html.document_fromstring(response.text)
        image = page.xpath("//div[@id='comic']/img")[0]
        #print image.get("src")
        #print image.get("title")
        #print image.get("alt")
        #print page.get_element_by_id("ctitle").text_content()
        #URL = "https://api.telegram.org/bot{}/".format(insult_bot)
        #url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(page.get_element_by_id("ctitle").text_content(), clicbait)
        #response = requests.get(url)     
        #url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(image.get("title"), clicbait)
        #response = requests.get(url)
        return [page.get_element_by_id("ctitle").text_content(), "http:" + image.get("src"), image.get("title")]

def main():
        insult_bot = "297812849:AAFGeKrSX3lyWv3m5XGiu3pr9G6wuLae1E8"
        clicbait = "-1001071499716"
        #URL = "https://api.telegram.org/bot{}/".format(insult_bot)
        #url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(get_random_image(), clicbait)
        #print get_random_image()
        #print get_random_xkcd_image()
        #sendImageRemoteFile(insult_bot, get_random_xkcd_image(), clicbait)
        #get_random_xkcd_image()
        #print get_random_image()
        #response = requests.get(url)
        #content = response.content.decode("utf8")
#print get_random_xkcd_image()
#main()