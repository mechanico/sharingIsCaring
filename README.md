# sharingIsCaring
## Background information
This is a GitHub repository keeping all relevant information about CVE-2018-7171.

CVE-2018-7171 represents a directory/file traversal vulnerability in TwonkyMedia Server 
version 7.0.11-8.5. Exploiting this vulnerability allows an attacker to list all files
located on the device, that is running the TwonkyMedia Server. Furthermore, an attacker is
able to download all media files (pictures, videos, and music) from a device after exploiting
this vulnerability. To exploit this vulnerability TwonkyMedia Server must not be protected 
by a password (which is the default setup).

Since a huge amount, around 24'000 TwonkyMedia Server instances, are reachable via the internet
the researcher decided to publish this vulnerability.

Maybe you don't know that TwonkyMedia Server is running on your device nor you know that it's
exposed in the internet. This is due to the fact that TwonkyMedia Server is pre-installed on
many NAS devices. If your router configuration automatically forwards the port (e.g. 9000) 
because it's a DLNA share, you're probably owned.

If your devices are affected by this vulnerability, expect all files on your device as no longer 
private.

Please make sure to switch off or protect your TwonkyMedia Server with a password, because no
fix for this vulnerability is available. 

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

## Example usage
When the script twonky.py is run, and the prompt is answered with "Y" the contentbase
Parameter for the TwonkyMedia Server will be set to /../ which allows from now on
the discovery, indexing and download of all media files available on the device and
peripherals.
![alt text](screenshots/twonkypy_usage_1.png?raw=true "twonky.py usage.")

The following Screenshots show how the TwonkyMedia Server can now be used to access all 
Media files available on the device e.g. in the /root directory
![alt text](screenshots/access_every_media_file.png?raw=true "access every file.")

## Explanation of output
* The "path nr" is e.g. 001, 002, ...
* To browse through directories use "/" as delimiter, e.g. 005/091

* Directories are marked with "Dir"
* Directories are colored "GREEN"

* Files are marked with "Fil"
* Files are not colored

* If a Keyword is discovered the line will be colored "RED"
