🧠 AutoRequirements — Generate requirements.txt Automatically

Tired of manually tracking dependencies in Python projects?
AutoRequirements is a minimal, zero-dependency Python script that scans your .py files, detects all imports, and generates a clean requirements.txt automatically.
How to use: "python3 autoreq.py folder" scans all python files in "folder" and its subdirectories. Fills all imports uniquely into the requirements.txt.

No external libraries, no messy parsing — just pure Python logic to save you time. ⚡🐍

🚀 Features

✅ Detects all import styles:

import module

from module import something

from module import *

import module as alias

from module import * as alias (strips as)

✅ Automatically removes aliases, commas, and duplicates
✅ Works across multiple files in a single run
✅ Graceful error handling — won’t crash if a file can’t be read
✅ Lightweight, fast, and easy to use

💡 Usage

1️⃣ Run the script with one or more Python files as arguments:

python autoreq.py file1.py file2.py file3.py


2️⃣ Instantly generate a requirements.txt:

Created requirements.txt for:
requests
flask
os
sys


3️⃣ Done! Your dependencies are now neatly listed and ready to install.

🧩 Example

Before:

import os, sys
from flask import *
from requests import get as fetch


After running AutoRequirements:

python autoreq.py app.py utils.py


Output (requirements.txt):

flask
requests
os
sys

🧰 Requirements

Python 3.x

No external libraries

❤️ Why You’ll Love It

Zero configuration.

Clean, human-readable output.

Perfect for solo projects, hackathons, or quick automation scripts.

Pythonic, minimalistic, and easy to drop into any repo.

👨‍💻 Author

Created with ☕ and a love for automation by GilbertZennerDev

“Because even your imports deserve automation.”
