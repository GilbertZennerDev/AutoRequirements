"""
I need to handle these cases:
import bla (handled)
from bla import * (handled)
from bla import * as bla2 (just cut out anything from 'as')
"""

import sys
from pathlib import Path

def find_line_after_imports(txt):
	imports = False
	for i, line in enumerate(txt):
		if "import" in line: imports = True
		if "import" not in line and len(line) and imports: return i;

def loopfiles():
	content = []
	if len(sys.argv) < 2: print("Give Folder in Args"); exit()
	elif len(sys.argv) == 2: filenames = Path(sys.argv[1] + '/').rglob('*.py')
	else: filenames = set(sys.argv[1:])
	for filename in filenames:
		try:
			tmp = open(filename, 'r').read().splitlines()
			content += tmp[:find_line_after_imports(tmp)]
		except Exception as e: print(e); exit()
	content = [line for line in content if 'import' in line and line[0] != '#']
	content = [line[:line.find('as')] if 'as' in line else line for line in content]
	content = [line[:line.find('import')] if ',' in line else line for line in content]
	return " ".join(content)

def fiximports():
	imports = loopfiles()
	imports = [line.replace(',', '') for line in ''.join(imp for imp in imports).split()]
	imports = [line.strip() for line in imports if line != 'import' and line != 'from' and line != '*']
	imports = set(imports)
	savedcontent = "\n".join(imports)
	open("requirements.txt", "w").write(savedcontent)
	print("Created requirements.txt for:\n", savedcontent)

if __name__ == "__main__": fiximports();
find_line_after_imports(open("testfolder/test.py", 'r').read().splitlines())