import markdown2
import os, sys
import codecs

output = """
<html>
    <head> 
        <meta charset="UTF-8"> 
        <meta http-equiv="X-UA-Compatible" content="chrome=1"> 
    </head>
<body>
"""
mkin = codecs.open(sys.argv[1], 'r', 'utf-8')
output += markdown2.markdown(mkin.read())
output += '</body></html>'

html_path = os.path.join(os.path.dirname(sys.argv[1]), 'cfa.html')
print "Printing to %s\n" % (html_path)
mkout = codecs.open(html_path, 'w', 'utf-8')
mkout.write(output)
mkout.close()
