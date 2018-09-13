import os,shutil

def single():
    ch='y'
    while(ch=='y'):
        file_name=input("Enter file name : ") #In unix systems we can also use os.mknod()
        f=open(file_name,"w+")
        f.close()
        ch=input("Do you want to create more files ? ")

def two():
    ch='y'
    path=os.getcwd()
    while(ch=='y'):
        dir_name=input("Enter directory name : ")
        os.mkdir(dir_name)
        os.chdir(dir_name)
        print("Now in ",os.getcwd())
        prompt=input("Do you want to create files ? ")
        if(prompt=='y'):
            single()
        else:
            print("Empty directory")
        os.chdir(path)
        print("Now in ",os.getcwd())
        ch=input("Do you want to create more directories ? ")
    
def hierarchial(path):
    os.chdir(path)
    print("Now in ",os.getcwd())
    prompt=int(input("Press 1 to create directory,2 to create files,3 to go back one level,4 to quit : "))
    if(prompt==1):
        dir_name=input("Enter directory name : ")
        os.mkdir(dir_name)
        os.chdir(dir_name)
        hierarchial(os.getcwd())
    elif(prompt==2):
        single()
        hierarchial(os.getcwd())
    elif(prompt==3):
        hierarchial(os.path.dirname(path))
    else:
        return None
    
def display():
    print("FILE STRUCTURE")
    for root, dirs, files in os.walk(".", topdown=True):
        print("Root--> ",root)
        print("Directories--> ",dirs)
        print("Files--> ",files)
        print("---------------")

rootfile=os.getcwd()
os.mkdir("FILES")
os.chdir("FILES")
path=os.getcwd()
ch='y'
print("FILE ORGANIZATION TECHNIQUES")
while(ch=='y'):
    print("1.Single-level\n2.Two-level\n3.Hierarchial")
    choice=int(input("Enter your choice : "))
    if(choice == 1):
        single()
        display()
    elif(choice == 2):
        two()
        display()
    elif(choice == 3):
        hierarchial(os.getcwd())
        os.chdir(path)
        display()
    else:
        print("PLease try again..")
        continue
    ch=input("Press x to exit : ")

os.chdir(rootfile)  
print(os.getcwd())
shutil.rmtree("FILES")