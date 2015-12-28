import markdown2
import os, sys
import codecs
import re

output = """
<html>
    <head> 
        <meta charset="UTF-8"> 
        <meta http-equiv="X-UA-Compatible" content="chrome=1">
        <link rel="stylesheet" type="text/css" href="pygments-css/default.css" />
        <link rel="stylesheet" type="text/css" href="css/markdown.css" />
        <link rel="stylesheet" type="text/css" href="css/owner.css" />
        <link href='http://fonts.useso.com/css?family=Open+Sans' rel='stylesheet' type='text/css'>
    </head>
<body>
    <div id="nav">
        <ul>
          <li class="pull_left"><a href="#">CFA</a></li>
          <li class="pull_left"><a>About</a></li>
        </ul>
    </div>
    <div id="content">
"""

headlines = []

def grab_headlines(content):
    regex_h1 = re.compile('^#\s+(.*?)<a.*a>$')
    regex_h2 = re.compile('^##\s+(.*?)<a.*a>$')
    for line in content.split('\r\n'):
        m = regex_h1.match(line)
        if m:
            headlines.append(m.group(1))

mkin = codecs.open(sys.argv[1], 'r', 'utf-8')
#grab_headlines(mkin.read())
output += markdown2.markdown(mkin.read(), extras=['fenced-code-blocks', 'cuddled-lists']) # extras=['cuddled-lists']
output += '</div></body></html>'

html_path = os.path.join(os.path.dirname(sys.argv[1]), os.path.splitext(sys.argv[1])[0] + ".html")
print "Printing to %s\n" % (html_path)
mkout = codecs.open(html_path, 'w', 'utf-8')
mkout.write(output)
mkout.close()
