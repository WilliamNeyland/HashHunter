import pathlib
import os

'''Class for creating directory FIM baselines'''

class baseline():
    def __init__(self, dir):
        print("You are in the baseline __init__ method")
        self.dir = dir

        # Type check the dir attribute
        assert type(self.dir) == pathlib.PosixPath, "Type error with self.dir" # The value of self.dir passed should be of type pathlib.PosixPath
        #self.dir = os.fspath(self.dir) # Cast type of self.dir from pathlib.PosixPath to str

        self.dirWalk()

    def dirWalk(self):
        print("You're in the test() method of the baseline class")
        cache = open('./cache/testCache.txt', 'r+', encoding='utf-8')

        # pathlib.walk() returns a three value tuple (root, dirs, files) where root = type pathlib.Posixpath | dirs = list of strings | files = list of strings

        # Prints out dir being walked prints and nested loops are used for testing
        for root, dirs, files in self.dir.walk():
            print(f'root of type {type(root)} = {root}\ndir of type {type(dirs)} = {dirs}\nfile of type {type(files)} = {files}\n')
            if len(dirs) > 0:
                i = 0
                for dir in dirs:
                    print(f'dir at position {i} of type {type(dir)} = {dir}')
                    i += 1
            if len(files) > 0:
                i = 0
                for file in files:
                    print(f'file at position {i} of type {type(file)} = {file}')
                    i += 1



#    os.stat() could be used for file attributes
#    shutil.copystat() could be used for writing stat attributes to a baseline file
#    Path can be used for dir paths
