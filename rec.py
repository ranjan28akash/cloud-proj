#!/usr/bin/env python
import cgi
import commands
print "Content-Type:text/html"
print ""

webdata=cgi.FieldStorage()
x=webdata.getvalue('u')
y=webdata.getvalue('p')
if x== "akash" and y=="redhat" :
	print('	<meta http-equiv="Refresh" content="0; url=http://localhost/abc.html">')
else :
	print "Failed"
