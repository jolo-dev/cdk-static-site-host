from __future__ import print_function

import sys
import os

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

project_slug = "{{ cookiecutter.project_slug }}"

assert (
    project_slug == project_slug.lower()
), f"{project_slug} project slug should be all lowercase"

dough = "{{ cookiecutter.dough }}"

if dough == "Git Repository":
    while True:
        choice = input(WARNING + "Please enter a git repository: " + TERMINATOR).lower()
        if choice != "":
            os.system("mkdir dough")
            os.system(f"git clone {choice} dough")
            break
        else:
            print(HINT + "Please respond with a valid Git Repository" + TERMINATOR)
