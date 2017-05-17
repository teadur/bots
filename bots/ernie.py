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
        data_image = []
        while data_image == []:
                random_date = randomDate("january-7-1996", datetime.datetime.now().strftime("%B-%d-%Y"), random.random())
                url_to_dilbert_page = "http://hagarthehorrible.com/comics/%s/" % random_date
                response = requests.get(url_to_dilbert_page)                
                page = html.document_fromstring(response.text)
                data_image = page.xpath("//form[@name='safr']/img")
        return [data_image[0].get("src"), random_date]

def get_random_ernie_image():
        data_image = []
        while data_image == []:
                random_date = randomDate("september-6-1998", datetime.datetime.now().strftime("%B-%d-%Y"), random.random())
                url_to_dilbert_page = "http://piranhaclubcomics.com/comics/%s/" % random_date
                response = requests.get(url_to_dilbert_page)                
                page = html.document_fromstring(response.text)
                data_image = page.xpath("//form[@name='safr']/img")
        return [data_image[0].get("src"), random_date]

def get_random_xkcd_image():
        image = []
        while image == []:
                response = requests.get("http://c.xkcd.com/random/comic/")        
                page = html.document_fromstring(response.text)
                image = page.xpath("//div[@id='comic']/img")
        return [page.get_element_by_id("ctitle").text_content(), "http:" + image[0].get("src"), image[0].get("title")]
