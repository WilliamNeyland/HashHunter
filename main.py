from pathlib import Path
from baseline import *
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

    baselineCache = Path(str(os.getcwd())+'/cache/baselineCache.txt')
    if baselineCache.exists():
        # Investigate if existingBaselines.close() statements are needed
        with open(baselineCache, 'r') as existingBaselines:
            for lines in existingBaselines:
                if lines.strip() == str(path):
                    print("WARNING: A Baseline for the directory provided already exists.\n"
                    "Choose:\n"
                    "1 -- Return to Main Menu\n"
                    "2 -- Overwrite Existing Baseline (THERE IS NO GOING BACK)")
                    tempInput = int(input("> "))
                    if tempInput == 1:
                        existingBaselines.close()
                        main()
                    elif tempInput == 2:
                        existingBaselines.close()
                        baseline(path)
                        break
                    else:
                        print("Invalid selection please try again.")
                        existingBaselines.close()
                        createBaseline()
                else:
                    with open(baselineCache, 'a') as existingBaselines:
                        existingBaselines.write(str(path)+'\n')
                        existingBaselines.close()
                        baseline(path)
                        break
    else:
        temp = os.getcwd()
        os.chdir(str(os.getcwd()+'/cache'))
        with open("baselineCache.txt", "w", encoding="utf-8") as baselineCacheFile:
            baselineCacheFile.write(str(path)+'\n')
        os.chdir(str(temp))
        baseline(path)
                

    

def main():
    print("Welcome to HashHunter an open source signature based FIM and AV tool!")
    print("===== MAIN MENU =====")
    print("Please select one of the following options to continue:")
    print("1.   Create Baseline")
    print("2.   Verify Directory Status")
    print("3.   Verify File Safety")
    userInput = int(input("> "))
    
    if userInput == 1:
        createBaseline()
    else:
        print("Sorry that's an invalid input please try again")
        main()

main()
