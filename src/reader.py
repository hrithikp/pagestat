from urllib2 import Request, URLError, urlopen

default_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'
}

class Reader(object):
    def __init__(self):
        self.headers = default_headers.copy()
        self.request = None
    def __call__(self, req_url, req_hdr={}):
        self.headers.update(req_hdr)
        if not req_url.startswith('http://'):
            req_url = 'http://' + req_url
        self.request = Request(req_url, headers=self.headers)
        try:
            response = urlopen(self.request)
            return response.read()
        except URLError, e:
            if hasattr(e, 'reason'):
                print 'Cannot reach server. Reason: %s.' % e.reason
            elif hasattr(e, 'code'):
                print 'Error code: ', e.code
            return e.fp.read()