from pathlib import Path

root = Path('.')  # or replace '.' with any directory path
python_files = root.rglob('*.py')  # recursively find all .py files

for file in python_files:
    print(file.resolve())  # prints the full absolute path
