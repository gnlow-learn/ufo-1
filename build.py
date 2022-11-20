import sys

from defcon import Font
from ufo2ft import compileOTF

name = sys.argv[1]

ufo = Font(name + '.ufo')
otf = compileOTF(ufo)
otf.save(name + '.otf')