import urllib.request
# This searches possible domain names with similiar facebook usernames


def facebook_search(a):
    try:
        data = urllib.request.urlopen("http://facebook.com/"+a)
        bool = False
    except urllib.error.HTTPError:
        bool = True
    return bool


