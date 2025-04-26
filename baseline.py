import pathlib
import os

'''Class for creating directory FIM baselines'''

class baseline():
    def __init__(self, dir):
        self.dir = dir

        # Type check the dir attribute
        assert type(self.dir) == pathlib.PosixPath, "Type error with self.dir" # The value of self.dir passed should be of type pathlib.PosixPath
        #self.dir = os.fspath(self.dir) # Cast type of self.dir from pathlib.PosixPath to str

        self.dirWalk()

    def dirWalk(self):
        cache = open('./cache/testCache.txt', 'r+', encoding='utf-8')

        # pathlib.walk() returns a three value tuple (root, dirs, files) where root = type pathlib.Posixpath | dirs = list of strings | files = list of strings
        for root, dirs, files in self.dir.walk():
            cache.write(str(root) + '\n')
            cache.write(str(dirs) + '\n')
            cache.write(str(files) + '\n')
            for file in files:
                cache.write(f'attributes of {root / file}: ' + str(os.stat(root / file)))

        cache.close()
