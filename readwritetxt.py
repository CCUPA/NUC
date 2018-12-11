import os, sys

def loop():
    while True:
        choice = menuchoice()
        choiceexec(choice)


def menuchoice():
    showmenu()
    while True:
        validchoices = [1, 2, 3, 4, 5, 6, 7, 8]
        try:
            choice = int(input("What would you like to do? "))

            if choice not in validchoices:
                print(repr(choice) + "Invalid menu choice")

            if choice in validchoices:
                return choice

        except ValueError:
            print("Invalid choice. Try again!")

def showmenu():                         #print menu
    print("1 - Show current directory path")
    print("2 - Show file names in current directory")
    print("3 - Show all directories and files in current path")
    print("4 - Enter new directory path")
    print("5 - Read a .txt file in current directory")
    print("6 - Write in a .txt file in current directory")
    print("7 - Create a new .txt file in current directory")
    print("8 - Quit")
    print("-" * 55)
    return

def choiceexec(x):
    if x == 1:
        showdirectory()
    if x == 2:
        filesindir()
    if x == 3:
        allinfo()
    if x == 4:
        newpath()
    if x == 5:
        opentxtfile()
    if x == 6:
        writetxtfile()
    if x == 7:
        newfile()
    if x == 8:
        exit()


def showdirectory():                #shows what directory you are currently in
    print("Current directory path: ", os.getcwd())
    print("\n")

def filesindir():                  #see files in current directory
    print("Files in directory: ", os.listdir())
    print("\n")

def allinfo():                  #all info in current directory
    for dirpath, dirnames, filenames in os.walk(".", topdown=False):
        print("Current path: ", dirpath)
        print("Directories: ", dirnames)
        print("Files: ", filenames)
        print("\n")


def newpath():                      #change directory
    try:
        pathinput = input("Enter new directory path, or type 'back' to go back to menu:  ")
        if pathinput == "back":
            print("\n")
            return
        else:
            os.chdir(pathinput)
            print("Current path is now:", pathinput)
            print("\n")
    except:
        print("Invalid input, try again")
        print("\n")
        newpath()


def opentxtfile():                  #veiw chosen txt file
        try:
            openfile = input("Enter the .txt file name, or type 'back' to go back to menu: ")
            if openfile == "back":
                print("\n")
                return
            else:
                with open(openfile, 'r') as f:
                    f_content = f.read()
                print(f_content)
                print("\n")
                f.close()

        except:
            print("Invalid input")
            print("\n")
            opentxtfile()


def writetxtfile():                     #append to chosen txt file
        try:
            openfile = input("Enter the .txt file name, or type 'back' to go back to menu: ")
            if openfile == "back":
                print("\n")
                return
            else:
                with open(openfile, 'r') as rf:
                    f_content = rf.read()
                    print("Current file text:", f_content)
                    print("\n")
                writeinput = input("What would you like to write?")
                with open(openfile, 'a') as wf:
                    wf.write(" " + writeinput)
                    wf.close()
        except:
            print("Invalid input")
            print("\n")
            writetxtfile()

def newfile():
    try:
        createtxt = input("Enter a name for your txt file:" "\n" "Type 'back' to go back to main menu")
        if createtxt == "back":
            print ("\n")
            return
        else:
            with open(createtxt, 'w') as cnf:
               print(cnf.name)
            cnf.close()
            writetofile = input("Write your text to the file: ")
            with open(createtxt, 'a') as cf:
                cf.write(writetofile)
                print("Current text in file: ", writetofile)
                print("\n")
                cf.close()
    except:
        print("Invalid input")
        print("\n")
        newfile()


def exit():
    sys.exit()

loop()