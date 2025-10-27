"""
I need to handle these cases:
import bla (handled)
from bla import * (handled)
from bla import * as bla2 (just cut out anything from 'as')
"""

import sys
import subprocess as sp

def loopfiles(imports=[]):
	filenames = [sys.argv[i] for i in range(2, len(sys.argv))]
	for filename in filenames:
		content = open(filename, 'r').read().splitlines()
		content = [line for line in content if 'import' in line]
		content = [line[:line.find('as')] if 'as' in line else line for line in content]
	return " ".join(content)

def fiximports():
	if len(sys.argv) < 2:
		print('Argument "show" or "install" required')
		exit()
	mode = sys.argv[1]
	imports = loopfiles()
	imports = [line.replace(',', '') for line in ''.join(imp for imp in imports).split()]
	imports = [line.strip() for line in imports if line != 'import' and line != 'from' and line != '*']
	imports = set(imports)
	savedcontent = "\n".join(imports)
	open("requirements.txt", "w").write(savedcontent)
	print("Created requirements.txt for:\n", savedcontent)
	
fiximports()

