from html import *
import urllib.request, urllib.error, urllib.parse

url = "http://www.dtc.umn.edu/~odlyzko/zeta_tables/zeros1"

response = urllib.request.urlopen(url)
webContent = response.read()

text = str(webContent).split()
text.pop(0)

array = []
for k in range(len(text)):
    array.append(text[k].replace("\\n", ""))

f = open("nontrivialzero.txt", "w+")
f.write(str(array))
f.close()