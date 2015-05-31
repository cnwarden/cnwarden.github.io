import markdown2
import os, sys
import codecs

output = '<html><head> <meta charset="UTF-8"> </head>'
mkin = codecs.open(sys.argv[1], 'r', 'utf-8')
output += markdown2.markdown(mkin.read())
output += '</html>'
print output