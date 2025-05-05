import pathlib
import os
import hashlib
import json
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

        temp = str(self.baselineDir)
        self.cacheFileName = hashlib.sha256(temp.encode(encoding='utf-8', errors='strict')).hexdigest()
        self.cacheFileDir = os.getcwd() + '/cache/baselines/' + self.cacheFileName + '.txt'
        file = open(self.cacheFileDir,'w')
        file.close()

    def dirWalk(self):

        baselineDict = {}
        baselineRootContent = []
        baselineFilesDict = {}
        with open(self.cacheFileDir, 'w', encoding='utf-8') as cache:
            # pathlib.walk() returns a three value tuple (root, dirs, files) where root = type pathlib.Posixpath | dirs = list of strings | files = list of strings
            # Baseline Data Structure -- root (key) : [[dirs],{file:[attributes]}]
            for root, dirs, files in self.baselineDir.walk():

                baselineRootContent.append(dirs)
                baselineDict.update({str(root) : 'test'})
                for x in baselineDict:
                    cache.write(str(x + ' : ' + baselineDict[x] + '\n'))

                #cache.write(str(root) + '\n')
                cache.write(str(dirs) + '\n')
                cache.write(str(files) + '\n')

                
                for file in files:
                    fileStat = os.stat(root / file)
                    filePath = str(root / file)
                    fileObj = fileStruct(filePath, fileStat)
                    #cache.write(fileObj.__str__() + '\n')

                    for item in fileObj.attributes:
                        cache.write(item + ' : ' + str(fileObj.attributes[item]) + '\n')

##### Baseline Storage Outline #####
#    Baselines will be stored in JSON format
#    Root will be a key with a value of an array
#        - Index 0 of this array will be an array of file names stored as strings
#        - Index 1 of this array will be File names present in root as keys with a value of an array
#            - Index 0 --> [n-1] will be file attributes stored as key-value-pairs   
#