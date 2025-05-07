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

        baselineList = []

        with open(self.cacheFileDir, 'w', encoding='utf-8') as cache:
            # pathlib.walk() returns a three value tuple (root, dirs, files) where root = type pathlib.Posixpath | dirs = list of strings | files = list of strings
            # Baseline Data Structure -- ["root", [dirs], {file:[attributes]}]
            for root, dirs, files in self.baselineDir.walk():

                baselineFilesDict = {}
                baselineRootContent = []
                
                for file in files:
                    fileStat = os.stat(root / file)
                    filePath = str(root / file)
                    fileObj = fileStruct(filePath, fileStat)

                    baselineFilesDict.update({file : fileObj.attributes})

                baselineRootContent.append(str(root))
                baselineRootContent.append(dirs)
                baselineRootContent.append(baselineFilesDict)
                baselineList.append(baselineRootContent)

            json.dump(baselineList, cache, indent=4)