from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
numlist = list()


# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    numtag = re.findall('[0-9]+', tag)
    if len(numtag) > 0:
        for numt in numtag:
            numlist.append(int(numt))
    print (numlist)

    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('tr', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
