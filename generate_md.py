import markdown2
import os, sys
import codecs

output = """
<html>
    <head> 
        <meta charset="UTF-8"> 
        <meta http-equiv="X-UA-Compatible" content="chrome=1">
        <link rel="stylesheet" type="text/css" href="pygments-css/default.css" />
        <link rel="stylesheet" type="text/css" href="css/github.css" />
    </head>
<body>
"""


mkin = codecs.open(sys.argv[1], 'r', 'utf-8')
output += markdown2.markdown(mkin.read(), extras=['fenced-code-blocks', 'cuddled-lists'])
output += '</body></html>'

html_path = os.path.join(os.path.dirname(sys.argv[1]), os.path.splitext(sys.argv[1])[0] + ".html")
print "Printing to %s\n" % (html_path)
mkout = codecs.open(html_path, 'w', 'utf-8')
mkout.write(output)
mkout.close()
