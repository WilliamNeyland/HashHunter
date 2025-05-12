import pathlib
import os
import hashlib
import json

class verifyBaseline():
    
    def __init__(self, baselinePath):
        self.baselinePath = baselinePath

        self.makeHash()
        self.loadCacheBaseline()


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
                self.cacheBaselineRoots.append(self.jsonBaseline[x][0])
                self.cacheBaselineDirs.append(self.jsonBaseline[x][1])
                self.cacheBaselineFileDicts.append(self.jsonBaseline[x][2])

            #for x in range(len(self.cacheBaselineFileDicts)):


            

    def getCurrentBaseline(self):
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