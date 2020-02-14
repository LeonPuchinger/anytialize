import shutil
from os.path import isdir, join, split
import subprocess as sp
from .util import AnytException
import os

def mkdir(name=""):
    if len(name) == 0:
        print("WARNING: mkdir action name empty, skipping action")
        return
    if isdir(name):
        print("WARNING: mkdir action name already exists, skipping action")
        return
    print(f"creating directory: \"{name}\"");
    os.mkdir(name)

#TODO overriding files/dirs
def copypaste(src="", dest="", override=False):
    if len(src) == 0 or len(dest) == 0:
        print("WARNING: cp action src or dest empty, skipping action")
        return
    if src == dest:
        print("WARNING: cp action src and dest equal, skipping action")
        return
    print(f"copying from  \"{src}\" to \"{dest}\"")
    try:
        if isdir(src):
            dest = join(dest, split(src)[-1])
            shutil.copytree(src, dest)
            return
        shutil.copy(src, dest)
    except FileExistsError as e:
        raise AnytException(f"ERROR: File/Directory already exists: \"{src}\"")

def shell(command="", args=[]):
    if len(command) == 0:
        print("WARNING: shell action command empty, skipping action")
        return
    prntargs = " ".join(args)
    print(f"executing \"{command} {prntargs}\"")
    process = sp.Popen([command]+args, stdout=sp.PIPE, stderr=sp.PIPE, universal_newlines=True)
    stdout, stderr = process.communicate()
    rc = process.returncode
    if rc != 0:
        raise AnytException(f"ERROR: shell action retuned with error code {rc}:\n{stderr}")