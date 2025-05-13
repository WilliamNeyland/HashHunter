from pathlib import Path
from baseline import *
from verifyBaseline import *
import os

def createBaseline():

    print("Please enter the path of the directory you would like to baseline:")
    print("[example: '/home/william/Documents']")
    path = Path(input("> "))

    if path.exists():
        print(f"{path} is valid")
    else:
        print("Invalid path please try again.")
        createBaseline()

    baselineCache = Path(os.getcwd()+'/cache/baselineCache.txt')
    if baselineCache.exists():
        with open(baselineCache, 'r') as existingBaselines:
            tempPathsRead = []
            for lines in existingBaselines:
                tempPathsRead.append(lines.strip())

            if str(path) in tempPathsRead:
                print("WARNING: A Baseline for the directory provided already exists.\n"
                "Choose:\n"
                "1 -- Return to Main Menu\n"
                "2 -- Overwrite Existing Baseline (THERE IS NO GOING BACK)")
                tempInput = int(input("> "))
                if tempInput == 1:
                    main()
                elif tempInput == 2:
                    baseline(path)
                else:
                    print("Invalid selection please try again.")
                    createBaseline()
            else:
                with open(baselineCache, 'a') as existingBaselines:
                    existingBaselines.write(str(path)+'\n')
                    baseline(path)
    else:
        # Creates necessary program directories on first run
        os.mkdir('./cache')
        os.mkdir('./cache/baselines')
        with open("./cache/baselineCache.txt", "w", encoding="utf-8") as baselineCacheFile:
            baselineCacheFile.write(str(path)+'\n')
        baseline(path)   

def selectBaseline():
    baselineCache = Path(os.getcwd()+'/cache/baselineCache.txt')
    if baselineCache.exists:
        with open(baselineCache, "r", encoding="utf-8") as baselineCacheFile:
            index = 1
            streamPosition = {}
            print("===== Available Baselines =====")
            while True:
                streamPosition.update({str(index) : baselineCacheFile.tell()})
                line = baselineCacheFile.readline().strip() # strips \n
                
                if not line: # Executes if readline returns EOF
                    del streamPosition[str(index)] # Removes last tell position as it points to EOF
                    break

                print(str(index)+ " - " + line)
                index+=1

            userInput = input("> ")
            if userInput not in streamPosition:
                print("ERROR: Invalid selection")
                selectBaseline()
            else:
                baselineCacheFile.seek(streamPosition[userInput])

            baselinePath = Path(baselineCacheFile.readline().strip())
            verifyBaseline(baselinePath)
            
            

    else:
        print("ERROR -- There are no pre-existing baselines to verify\nReturning to Main Menu.")
        main()

def main():
    
    print("Welcome to HashHunter an open source signature based FIM and AV tool!")
    print("===== MAIN MENU =====")
    print("Please select one of the following options to continue:")
    print("1.   Create Directory Baseline")
    print("2.   Verify Directory Status")
    print("3.   Verify File Safety")
    userInput = int(input("> "))
    
    if userInput == 1:
        createBaseline()
    elif userInput == 2:
        selectBaseline()
    else:
        print("Sorry that's an invalid input please try again")
        main()

main()
