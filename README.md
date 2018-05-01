# sharingIsCaring TwonkyMedia Server Pwnd CVE-2018-7171
## Background information
This is a GitHub repository keeping all relevant information about CVE-2018-7171.

CVE-2018-7171 represents a directory/file traversal vulnerability in TwonkyMedia Server 
version 7.0.11-8.5 (latest version). Exploiting this vulnerability allows an attacker to 
list all files located on the device, that is running the TwonkyMedia Server. Furthermore, 
an attacker is able to download all media files (pictures, videos, and music) from a device 
after exploiting this vulnerability. To exploit this vulnerability TwonkyMedia Server must 
not be protected by a password (which is the default setup).

Since a huge amount, around 24'000 TwonkyMedia Server instances, are reachable via the internet
the researcher decided to publish this vulnerability.

Maybe you don't know that TwonkyMedia Server is running on your device nor you know that it's
exposed in the internet. This is due to the fact that TwonkyMedia Server is pre-installed on
many NAS devices. Your router may automatically forward the UPnP port (e.g. 9000). This makes
the TwonkyMedia Server accessible public.

<b>If your devices are affected by this vulnerability, expect all files on your device as no longer 
private.</b>

### Countermeasures
Please make sure to switch off or protect your TwonkyMedia Server with a password, because no
fix for this vulnerability is available. 

## Disclaimer
Any actions and or activities related to the material contained within this repository is solely your 
responsibility.The misuse of the information in this repository can result in criminal charges brought 
against the persons in question. The author will not be held responsible in the event any criminal 
charges be brought against any individuals misusing the information in this repository to break the law.

Running twonky.py for attacking targets without prior mutual consent is illegal. It is the end user's 
responsibility to obey all applicable local, state and federal laws.

## About
<b>twonky.py</b> can be used to comfortably browse devices running TwonkyMedia Server. 
Also, a feature is implemented which checks file and directory names against a built-in 
extensible wordlist for keywords e.g. "wallet". Furthermore, interesting system information
is requested and presented to the user.

<b>downloadFiles.py</b> can be used to perform bulk downloads of TwonkyMedia Server indexed directories.

## Installation
```
$ git clone https://github.com/mechanico/sharingIsCaring.git

$ cd sharingIsCaring

$ sudo pip install -r requirements.txt
```

You're ready to go!

## Example usage twonky.py
When the script <b>twonky.py [IP ADRESS] [PORT]</b> is run, and the prompt is answered with 
"Y" the contentbase Parameter for the TwonkyMedia Server will be set to /../ that allows 
from now on the discovery, indexing and download of all media files available on the device and
connected peripherals.
![alt text](screenshots/twonkypy_usage_1.png?raw=true "twonky.py usage.")

### Explanation of output
* The "path nr" is e.g. 001, 002, ...
* To browse through directories use "/" as delimiter, e.g. 005/091

* Directories are marked with "Dir"
* Directories are colored "GREEN"

* Files are marked with "Fil"
* Files are not colored

* If a Keyword is discovered the line will be colored "RED"

### What will twonky.py do?
* set contentbase parameter to /../
* collect some information on the target (e.g. how many pictures indexed, ...)
* give you the ability to browse through all directories on the target
* highlight "interesting files" red
* PHPSESSID cookie file discovery, the script will automatically test them against the WD api,
if successfull you will be able to take over the NAS device

### What will twonky.py not do?
* Download files
* Take over NAS devices automatically

## Demonstration access ALL files
The following Screenshots show how the TwonkyMedia Server can now be used to access all 
Media files available on the device e.g. in the /root directory. Be aware that 
TwonkyMedia Server is not only running on Unix but also on Windows installations all
demonstrations are applicable for multiple operation systems.
![alt text](screenshots/access_every_media_file.png?raw=true "access every file.")

## Example usage downloadFiles.py
To start the bulk download of files, shared by the TwonkyMedia Server simply copy the URL of the
folder of interest:
![alt text](screenshots/copy_twonky_folder_url.png?raw=true "copy URL.")

Next launch <b>downloadFiles.py [PATH TO SAVE DOWNLOADS]</b> with the path, where the downloaded
files should be saved. Next provide the script with the TwonkyMedia Server Folder URL you copied 
previously.  Now the script creates a new folder with the IP Adress as name and automatically
starts downloading all files if less then 30 media files exist in this folder. If there are more then
30 media files, the script will show a prompt with the total count of media files discovered. Answer
"Y", the bulk download will start.
![alt text](screenshots/downloadFilesdemo.png?raw=true "Download files.")

