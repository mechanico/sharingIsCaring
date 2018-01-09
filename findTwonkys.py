import urllib2
import shodan
import socket
import httplib

SHODAN_API_KEY= '<YOURKEY>'

api = shodan.Shodan(SHODAN_API_KEY)

def ipRange(start_ip, end_ip):
	start = list(map(int, start_ip.split(".")))
	end = list(map(int, end_ip.split(".")))
	temp = start
	ip_range = []
   
	ip_range.append(start_ip)
	while temp != end:
		start[3] += 1
		for i in (3, 2, 1):
			if temp[i] == 256:
				temp[i] = 0
				temp[i-1] += 1
		ip_range.append(".".join(map(str, temp)))    
     	return ip_range

def findTwonkyString(twonkyResponse):
	if twonkyResponse.find("Twonky") != -1:
		return True
	else:
		return False

def requestTwonkyUrls(url):
	try: 
		twonkyResponse = urllib2.urlopen(url, timeout = 1).read()
		twonkyCheck = findTwonkyString(twonkyResponse)
		if twonkyCheck == True:
			print "Twonky Up: %s" % url
			with open('twonkyHTTP.txt', 'a') as twonkyFileHTTP:
				twonkyFileHTTP.write(url + "\n")
	except urllib2.URLError:
		pass
	except socket.timeout:
		pass
	except socket.error:
		pass
	except httplib.BadStatusLine:
        	pass	
# sample usage
'''
ip_range = ipRange("31.20.1.1", "31.20.255.255")
for ip in ip_range:
	requestTwonkyUrls(ip, "9000")
	requestTwonkyUrls(ip, "9001")

try:	
	for x in range(1,209):
		results = api.search('Twonky', page=x)
		#print "Results found: %s" %results['total']
		for result in results['matches']:
			#requestTwonkyUrls(result['ip_str'], result['port'])
			print result['ip_str'], result['port']
			with open('twonkys.txt','a') as twonkyFile:
				twonkyFile.write("http://" + result['ip_str'] + ":" + str(result['port']) + "/" + "\n")

except shodan.APIError, e:
	print "Error: %s" %e
'''
with open('twonkys.txt', 'r') as twonkyFile:
	for line in twonkyFile:
		url = line.strip()
		requestTwonkyUrls(url)

