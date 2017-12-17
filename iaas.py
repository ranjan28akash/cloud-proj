#!/usr/bin/env python
import cgi
import commands
print "Content-Type:text/html"
print ""

webdata=cgi.FieldStorage()
os=webdata.getvalue('os')
ram=webdata.getvalue('ram')
cpu=webdata.getvalue('cpu')
hd=webdata.getvalue('hd')

if hd=="live" :
	cmd="virt-install --cdrom /var/www/html/iso/"+os+".iso --ram "+ram+" --vcpu "+cpu+" --nodisk --name my"+os+" --graphics vnc,listen=127.0.0.1,port=5912,password=redhat"
else :
	cmd="virt-install --cdrom /var/www/html/iso/"+os+" --ram "+ram+" --vcpu "+cpu+" --disk "+hd+" --name my"+os+" --graphics vnc,listen=127.0.0.1,port=5912,password=redhat"

print cmd
