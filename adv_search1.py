#!/usr/local/bin/python
import urllib.request
import bs4
import cgi


def facebook_search(a):
    try:
        data = urllib.request.urlopen("http://facebook.com/"+a)
        bool = False
    except urllib.error.HTTPError:
        bool = True
    return bool


def twitter_search(a):
    try:
        data = urllib.request.urlopen("http://twitter.com/"+a)
        bool = False
    except urllib.error.HTTPError:
        bool = True
    return bool

def instagram_search(a):
    try:
        data = urllib.request.urlopen("http://instagram.com/"+a)
        bool = False
    except urllib.error.HTTPError:
        bool = True
    return bool


def tangible_search(url,a):
    try:
        url=url.strip()
        if(url.find(".")):
            data = urllib.request.urlopen(url+a)
        else:
            data = urllib.request.urlopen("http://"+url+".com/" + a)
        bool = False
    except urllib.error.HTTPError:
        bool = True
    return bool

def ListOfElements(a):
    web = urllib.request.urlopen("http://naming.verisign-grs.com/ns-api/1.0/suggest?key="+a)
    page = web.read()
    parsedPage = bs4.BeautifulSoup(page, "html.parser")
    original_string = str(parsedPage)
    parsed_string = original_string.split("[{",1)[-1]
    parsed_string = parsed_string.split("}]",1)[0]
    parsedlist=parsed_string.split("},{")
    listofelemnts=[]
    for x in parsedlist:
        listofelemnts.append(x.replace("\"","").split(","))
    for x in listofelemnts:
        name=((x[0]).split(":", 1)[-1]).split(".", 1)[0]
        if facebook_search(name):
            x.append("Facebook:Available")
        else:
            x.append("Facebook:Unavailable")
        if twitter_search(name):
            x.append("Twitter:Available")
        else:
            x.append("Twitter:Unavailable")
        if instagram_search(name):
            x.append("Instagram:Available")
        else:
            x.append("Instagram:Unavailable")

    return listofelemnts

name_l = ["key", "key1", "key2", "key3", "key4", "key5", "key6", "key7", "key8"]
i = 0
p_list = []
s_list = []
form = cgi.FieldStorage()

while i < 8:
    input_text = form.getfirst(name_l[i], "")
    if input_text != "":
        #p_list = p_list.append(input_text)
        p_list.append(input_text)
    i = i + 1

#while i < len(p_list):
#    ss_list = ListOfElements(p_list[i]+form.getfirst("key"))
#    s_list = s_list.append(ss_list)
#    i = i + 1

#for e in p_list:
#    ss_list = ListOfElements(e+form.getfirst("key"))
#    s_list = s_list.append(ss_list)
#    i = i + 1

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<body>")
#print "<p>%s</p>" % form  #uncomment this line if you want
#to see what does form hashes look like
print("<p>%s</p>" % p_list)
print("</body>")
print("</html>")

