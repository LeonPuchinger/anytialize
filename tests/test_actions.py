import anytialize.actions as actions
from unittest import TestCase, main
import os.path

#TODO: rewrite test to be independent
class TestActions(TestCase):
    def test_mkdir(self):
        name = "./testfiles/testfolder"
        actions.mkdir(name)
        self.assertTrue(os.path.isdir(name))

    def test_cp_file(self):
        src = "./testfiles/cpsrc/cpsrc.txt"
        dest = "./testfiles/cpdest"
        actions.copypaste(src, dest)
        self.assertTrue(os.path.isfile(f"{dest}/cpsrc.txt"))
        actions.copypaste(src, f"{dest}/cpdest.txt")
        self.assertTrue(os.path.isfile(f"{dest}/cpdest.txt"))
        
    def test_cp_folder(self):
        src = "./testfiles/cpsrc"
        dest = "./testfiles/cpdest"
        actions.copypaste(src, dest)
        self.assertTrue(os.path.isdir(f"{dest}/cpsrc"))

    def test_rm_file(self): #doubles as cleanup
        path = "./testfiles/cpdest/cpdest.txt"
        actions.rm(path)
        self.assertFalse(os.path.isfile(path))

    def test_rm_folder_recursive(self): #doubles as cleanup
        path = "./testfiles/cpdest"
        actions.rm(path, True)
        self.assertFalse(os.path.isdir(path))

    def test_rm_folder(self): #doubles as cleanup
        path = "./testfiles/testfolder"
        actions.rm(path)
        self.assertFalse(os.path.isdir(path))

    def test_shell(self): #doubles as cleanup
        path = "./testfiles/cpdest"
        actions.shell("mkdir", [path])

if __name__ == "__main__":
    main()