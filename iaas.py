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
	cmd="sudo virt-install --cdrom /root/Downloads/iso/"+os+".iso --ram "+ram+" --vcpu "+cpu+" --nodisk --name my"+os+" --graphics vnc,listen=127.0.0.1,port=5912,password=redhat"
else :
	cmd="sudo virt-install --cdrom /root/Downloads/iso/"+os+".iso --ram "+ram+" --vcpu "+cpu+" --disk "+hd+" --name my"+os+" --graphics vnc,listen=127.0.0.1,port=5912,password=redhat"

commands.getoutput(cmd)
