import pyshorteners

# Von Leopold

def shorten_url(url):
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(url)
    return short_url

