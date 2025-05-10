import pathlib
import os
import hashlib

class verifyBaseline():
    
    def __init__(self, baselinePath):
        self.baselinePath = baselinePath

        self.makeHash()

    # CLEAN UP
    # PoC in Current State
    def makeHash(self):
        cacheBaselineName = hashlib.sha256(str(self.baselinePath).encode(encoding='utf-8', errors='strict')).hexdigest()
        cacheBaselinePath = os.getcwd() + '/cache/baselines/' + cacheBaselineName + '.txt'
        with open (cacheBaselinePath, 'r') as cacheBaseline:

            print(f'===== BASELINE: {self.baselinePath} =====')

            for lines in cacheBaseline:
                print(lines)
