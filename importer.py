import sys
import subprocess as sp

def loopfiles(imports=[]):
	filenames = [sys.argv[i] for i in range(2, len(sys.argv))]
	for filename in filenames:
		imports += [line + ' ' for line in open(filename, 'r').read().splitlines() if 'import' in line]
	return imports

def fiximports():
	if len(sys.argv) < 2:
		print('Argument show or install required')
		exit()
	mode = sys.argv[1]
	imports = loopfiles()
	imports = [line.replace(',', '') for line in ''.join(imp for imp in imports).split()]
	imports = [line for line in imports if line != 'import' and line != 'from']
	imports = set(imports)
	open("requirements.txt", "w").write("\n".join(imports))
	if mode == 'show':
		print(imports)
	elif mode == 'install':
		sp.run(['pip', 'install', *imports])
	print("Fixed the Imports. Created requirements.txt")
	
fiximports()

