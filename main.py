from pathlib import Path
from baseline import *

def createBaseline():
    print("Please enter the path of the directory you would like to baseline:")
    print("[example: '/home/william/Documents']")
    path = Path(input("> "))
    if path.exists():
        print(f"{path} is valid")
        #print(type(path))
        baseline(path)
    else:
        print("Invalid path please try again.")
        createBaseline()

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
