#!/usr/bin/env python
import cgi
import commands
print "Content-Type:text/html"
print ""

webdata=cgi.FieldStorage()
x=webdata.getvalue('a')

if x== "saas" :
	print('	<meta http-equiv="Refresh" content="0; url=http://localhost/saas.html">')
elif x== "staas" :
	print('	<meta http-equiv="Refresh" content="0; url=http://localhost/staas.html">')
elif x== "iaas" :
	print('	<meta http-equiv="Refresh" content="0; url=http://localhost/iaas.html">')
elif x== "paas" :
	print('	<meta http-equiv="Refresh" content="0; url=http://localhost/paas.html">')


