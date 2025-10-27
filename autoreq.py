"""
I need to handle these cases:
import bla (handled)
from bla import * (handled)
from bla import * as bla2 (just cut out anything from 'as')
"""

import sys

def loopfiles():
	if len(sys.argv) < 2: print('Enter filenames as args!'); exit()
	filenames = set(sys.argv[1:])
	for filename in filenames:
		try:
			content = open(filename, 'r').read().splitlines()
			content = [line for line in content if 'import' in line]
			content = [line[:line.find('as')] if 'as' in line else line for line in content]
		except Exception as e:
			print(e); exit()
	return " ".join(content)

def fiximports():
	imports = loopfiles()
	imports = [line.replace(',', '') for line in ''.join(imp for imp in imports).split()]
	imports = [line.strip() for line in imports if line != 'import' and line != 'from' and line != '*']
	imports = set(imports)
	savedcontent = "\n".join(imports)
	open("requirements.txt", "w").write(savedcontent)
	print("Created requirements.txt for:\n", savedcontent)

if __name__ == "__main__": fiximports()