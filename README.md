🧠 AutoRequirements — Generate requirements.txt Automatically

Tired of manually tracking dependencies in your Python projects?
Meet AutoRequirements, a lightweight script that scans your .py files, detects all imports, and instantly generates a clean requirements.txt file — no fuss, no external tools. ⚡🐍

🚀 Features

✅ Detects all import patterns:

import module

from module import something

from module import *

import module as alias

from module import * as alias

✅ Automatically removes aliases (as something) and duplicates
✅ Works across multiple files
✅ Pure Python — no dependencies

💡 Usage

1️⃣ Run the script with your .py files as arguments:

python autoreq.py install file1.py file2.py file3.py


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


After running:

python autoreq.py install app.py


Output (requirements.txt):

flask
requests
os
sys

🧰 Requirements

Just Python. Nothing else.

❤️ Why You’ll Love It

Zero configuration.

No parsing overhead.

Perfect for small scripts or quick automation projects.

Minimalistic — in true Pythonic spirit.

👨‍💻 Author

Built with ☕, patience, and a love for automation by @GilbertZennerDev
.

“Because even your imports deserve automation.”
