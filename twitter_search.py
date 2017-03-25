import urllib.request
# This searches a possible domain names with similiar twitter handles

def twitter_search(a):
    try:
        data = urllib.request.urlopen("http://twitter.com/"+a)
        bool = False
    except urllib.error.HTTPError:
        bool = True
    return bool