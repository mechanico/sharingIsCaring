import requests
from xml.etree import ElementTree
import wget
import sys
import socket
import os

def downloadWorker(tree, twonkyServer, downloadPath):
	for child in tree.iter("res"):
		if "LRG" in child.text or "AVI" in child.text or "MOV" in child.text:
			url = child.text.replace("127.0.0.1",twonkyServer)
			splited = url.split("/")
			splitedTwo = splited[len(splited)-1]
			fileUrl = downloadPath + "/" + splitedTwo[:splitedTwo.find("?")]
			if not os.path.isfile(fileUrl):
				try: 
					wget.download(url, downloadPath)
				except socket.error, e:
					if 'Errno 111' in e:
						print '*** Connection refused ***'
						print '*** Url: %s ***' %url
						pass
					elif 'Errno 10054' in e:
						print '*** Connection closed by Remote Host ***'
						print '*** Url: %s ***' %url
						pass
			else:
				pass
			
	return

def downloadFiles(twonky, twonkyServer, downloadPath):
	twonkyFolderStart = twonky.find("#")
	if twonkyFolderStart != -1:
		twonkyFinalUrl = createTwonkyUrl(twonky, twonkyServer, twonkyFolderStart)
		response = requests.get(twonkyFinalUrl)
		tree = ElementTree.fromstring(response.content)
		for child in tree.iter("childCount"):
			pictureCount = child.text
			break
		if int(pictureCount) >= 30:
			getAll = raw_input("Found %s pictures, get all? [Y, N] "%pictureCount)
		else:
			getAll = "N"
		if getAll.upper() == "Y":
			rangeList = range(0,int(pictureCount),30)
			if rangeList[len(rangeList)-1] < int(pictureCount):
				rangeList[len(rangeList)-1] = int(pictureCount)-30
			for pics in rangeList:
				downloadUrl = twonkyFinalUrl.replace("start=0", "start=" + str(pics))
				response = requests.get(downloadUrl)
				tree = ElementTree.fromstring(response.content)
				downloadWorker(tree, twonkyServer, downloadPath)
		elif getAll.upper() == "N":
			downloadWorker(tree, twonkyServer, downloadPath)
		else:
			print "*** Invalid Input! ***"
		
	else:
		print "*** Invalid Url! ***"
		sys.exit()


def createTwonkyUrl(twonky, twonkyServer, twonkyFolderStart):
	twonkyUrl = twonky[twonkyFolderStart+1:]
	twonkyUrlFindOne = twonkyUrl.find(":9000")
	twonkyUrlFindTwo = twonkyUrl.find(":9001")
	if twonkyUrlFindOne != -1:
		twonkyFinalUrlEnd = twonkyUrl[twonkyUrlFindOne:]
		twonkyFinalUrl = "http://" + twonkyServer + twonkyFinalUrlEnd
		return twonkyFinalUrl
	elif twonkyUrlFindTwo != -1:
		twonkyFinalUrlEnd = twonkyUrl[twonkyUrlFindTwo:]
		twonkyFinalUrl = "http://" + twonkyServer + twonkyFinalUrlEnd
		return twonkyFinalUrl
	else:
		print "*** Invalid Url! ***"
		sys.exit()

def checkCreateDir(downloadPath, twonkyServer):
	directory = downloadPath + twonkyServer
	if not os.path.exists(directory):
		try:
			os.makedirs(directory)
			print "*** Directory %s created. ***" %directory
		except OSError as e:
			print "Error: " %e
			sys.exit()
	else:
		print "*** Directory %s found. ***" %directory
	return directory

def main():
	if len(sys.argv) != 2 :
		print "Usage: " + sys.argv[0] + " [Downloadpath]'"
		sys.exit()
	else:
		downloadPath = sys.argv[1]
	print "-" * 30
	print "#SharingIsCaring"                                                 
	print "-" * 30

	twonky = raw_input("Enter Twonky Folder Url: ")
	twonkyServerStart = twonky.find("http://")
	twonkyServerEndOne = twonky.find(":9000")
	twonkyServerEndTwo = twonky.find(":9001")
	if twonkyServerEndOne != -1:
		twonkyServer = twonky[twonkyServerStart+7:twonkyServerEndOne]

	elif twonkyServerEndTwo != -1:
		twonkyServer = twonky[twonkyServerStart+7:twonkyServerEndTwo]
	else:
		print "*** Invalid Url! ***"
		sys.exit()

	downloadFiles(twonky, twonkyServer, checkCreateDir(downloadPath, twonkyServer))
	continueDownload = raw_input("\nContinue downloading? [Y, N] ")
	if continueDownload.upper() == "Y":
		main()
	else:
		print "\n*** Thanks for Sharing :) ***"
		sys.exit()

main()
