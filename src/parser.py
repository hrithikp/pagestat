from HTMLParser import HTMLParser

class Parser(HTMLParser):
    ctypes = ['tags', 'attrs']
    def __init__(self):
        self.store = {k: {} for k in self.ctypes}
        self.reset()
    def __call__(self, html, ctype):
        self.feed(html)
        return self.getData(ctype)
    def handle_starttag(self, name, info):
        tags = self.store['tags']
        attrs = self.store['attrs']
        if name in tags:
            tags[name] += 1
        else:
            tags[name] = 1
        for key,val in info:
            if key in attrs:
                attrs[key] += 1
            else:
                attrs[key] = 1

    def getData(self, ctype):
        if not ctype in self.store:
            return None
        else:
            return self.store[ctype]