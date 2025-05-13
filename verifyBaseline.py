from pathlib import Path
import os
import hashlib
import json
from fileStruct import *

class verifyBaseline():
    
    def __init__(self, baselinePath):
        self.baselinePath = baselinePath

        self.makeHash()
        self.loadCacheBaseline()
        self.getCurrentBaseline()
        self.compareBaselines()


    # CLEAN UP
    # PoC in Current State
    def makeHash(self):
        cacheBaselineName = hashlib.sha256(str(self.baselinePath).encode(encoding='utf-8', errors='strict')).hexdigest()
        self.cacheBaselinePath = os.getcwd() + '/cache/baselines/' + cacheBaselineName + '.txt'
    
    def loadCacheBaseline(self):
        with open (self.cacheBaselinePath, 'r') as cacheBaseline:
            self.jsonBaseline = json.load(cacheBaseline) # Loads the JSON file as a list

            self.cacheBaselineRoots = []
            self.cacheBaselineDirs = []
            self.cacheBaselineFileDicts = []

            for x in range(len(self.jsonBaseline)):
                self.cacheBaselineRoots.append(self.jsonBaseline[x][0]) # Roots
                self.cacheBaselineDirs.append(self.jsonBaseline[x][1]) # Dirs within the Root
                self.cacheBaselineFileDicts.append(self.jsonBaseline[x][2])

            #for x in range(len(self.cacheBaselineFileDicts)):

    def getCurrentBaseline(self):
        # Check if baseline root dir still exists
        if self.baselinePath.exists():
            self.currentBaselineList = []

            # pathlib.walk() returns a three value tuple (root, dirs, files) where root = type pathlib.Posixpath | dirs = list of strings | files = list of strings
            # Baseline Data Structure -- ["root", [dirs], {file:[attributes]}]
            for root, dirs, files in self.baselinePath.walk():

                currentFilesDict = {}
                currentRootContent = []
                
                for file in files:
                    fileStat = os.stat(root / file)
                    filePath = str(root / file)
                    fileObj = fileStruct(filePath, fileStat)

                    currentFilesDict.update({file : fileObj.attributes})

                currentRootContent.append(str(root))
                currentRootContent.append(dirs)
                currentRootContent.append(currentFilesDict)
                self.currentBaselineList.append(currentRootContent)

            print(str(self.currentBaselineList))
        else:
            print("Baseline Root Directory no longer exists.\nExiting now.")
            exit()

    def compareBaselines(self):
        pass

#[root,[dirs],{fileName:{attributeKey:value}}]
# Verify Root Dirs
# Verify Dirst within Root
# Verify Files Within root
# Verify attributes for files within root

#keys = list(jsonBaseline[0][2].keys())
#values = list(jsonBaseline[0][2].values())
#keys2 = list(values[0].keys())
#values2 = list(values[0].values())