import os

currpath = os.path.abspath(".")

if "code" not in currpath:
    if "test" in currpath:
        os.chdir(os.path.join("..", "code"))
    else:
        os.chdir("code")

