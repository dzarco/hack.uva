import urllib.request
import bs4
import json

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
    return listofelemnts