import re
import urllib
uResponse = urllib.urlopen('http://python.org/')
_html = uResponse.read()

p=re.compile('<a\s*.*?>(.*?)</a>')
nodes=p.findall(_html)
for i, node in enumerate(nodes):
    print i, node