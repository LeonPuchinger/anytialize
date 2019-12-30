import anytialize.actions as actions
from unittest import TestCase, main
import os.path

class TestActions(TestCase):
    def test_cp_file(self):
        src = "./testfiles/cpsrc/cpsrc.txt"
        dest = "./testfiles/cpdest"
        actions.copypaste(src, dest)
        self.assertTrue(os.path.isfile(f"{dest}/cpsrc.txt"))
        
    def test_cp_folder(self):
        src = "./testfiles/cpsrc"
        dest = "./testfiles/cpdest"
        actions.copypaste(src, dest)
        self.assertTrue(os.path.isdir(f"{dest}/cpsrc"))

    def test_shell(self):
        path1 = "./testfiles/cpdest/cpsrc.txt"
        path2 = "./testfiles/cpdest/cpsrc"
        actions.shell("rm", [path1])
        self.assertFalse(os.path.isfile(path1))
        actions.shell("rm", ["-r", path2])
        self.assertFalse(os.path.isdir(path2))

if __name__ == "__main__":
    main()