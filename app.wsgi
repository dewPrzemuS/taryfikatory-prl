import sys

sys.path.insert(0, "/var/www/lspd")

activate_this = "/home/przemus/.local/share/virtualenvs/lspd-SFC6TkyG/bin/activate_this.py"

with open(activate_this) as file:
    exec(file.read(), dict(__file__=activate_this))

from app import app as application