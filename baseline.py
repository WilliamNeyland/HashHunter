import pathlib
import os
import stat
from fileStruct import *

'''Class for creating directory FIM baselines'''

class baseline():
    def __init__(self, dir):
        self.dir = dir

        # Type check the dir attribute
        assert type(self.dir) == pathlib.PosixPath, "Type error with self.dir" # The value of self.dir passed should be of type pathlib.PosixPath
        #self.dir = os.fspath(self.dir) # Cast type of self.dir from pathlib.PosixPath to str

        self.dirWalk()

    def dirWalk(self):
        with open('./cache/testCache.txt', 'w', encoding='utf-8') as cache:
            # pathlib.walk() returns a three value tuple (root, dirs, files) where root = type pathlib.Posixpath | dirs = list of strings | files = list of strings
            for root, dirs, files in self.dir.walk():
                cache.write(str(root) + '\n')
                cache.write(str(dirs) + '\n')
                cache.write(str(files) + '\n')
                
                for file in files:
                    fileStat = os.stat(root / file)
                    filePath = str(root / file)
                    fileObj = fileStruct(filePath, fileStat)
                    cache.write(fileObj.__str__() + '\n')


#st_mode == File mode: file type and file mode bits (permissions).
#st_ino ==
#st_dev == Identifier of the device on which this file resides.
#st_nlinks == Number of hard links.
#st_uid == User identifier of the file owner.
#st_gid == Group identifier of the file owner.
#st_size == Size of the file in bytes, if it is a regular file or a symbolic link. The size of a symbolic link is the length of the pathname it contains, without a terminating null byte.
#st_atime == Time of most recent access expressed in seconds.
#st_ctime == Time of most recent content modification expressed in seconds.
#st_mtime == Time of most recent metadata change expressed in seconds.