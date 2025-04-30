import pathlib
import os
import hashlib
from fileStruct import *
from pathlib import *

'''Class for creating directory FIM baselines'''

class baseline():
    def __init__(self, dir):
        self.baselineDir = dir
        self.cacheFileName = ''
        self.cacheFileDir = ''
        # Type check the dir attribute
        assert type(self.baselineDir) == pathlib.PosixPath, "Type error with self.baselineDir"

        self.makeBaselineFile()
        self.dirWalk()

    def makeBaselineFile(self):
        # This will create a baseline file to keep the specified paths baseline in a unique file
        # This will need to be stored in an obfuscated manner
        # File name will be obfuscated
        # A dictionary will be created with the path as the key and obfuscated baseline filename as the entry -- PROBABLY NOT NEEDED
        # This dictionary will need to be stored and loaded into memory when the program runs

        temp = str(self.baselineDir)
        self.cacheFileName = hashlib.sha256(temp.encode(encoding='utf-8', errors='strict')).hexdigest()
        self.cacheFileDir = os.getcwd() + '/cache/baselines/' + self.cacheFileName + '.txt'
        file = open(self.cacheFileDir,'w')
        file.close()

    def dirWalk(self):
        with open(self.cacheFileDir, 'w', encoding='utf-8') as cache:
            # pathlib.walk() returns a three value tuple (root, dirs, files) where root = type pathlib.Posixpath | dirs = list of strings | files = list of strings
            for root, dirs, files in self.baselineDir.walk():
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

##### Baseline Storage Outline #####
#    1. Dictionary with the root or cwd as the key
#    2. The keys value will be a two value tuple
#        - Tuple[0] = list of dir's in cwd
#        - Tuple[1] = list of files and their attributes