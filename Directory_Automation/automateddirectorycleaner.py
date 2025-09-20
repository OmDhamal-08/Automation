#this will arange all the files in the extension according to its extension by makin new folders in the same directory 
# this will arrange or just diffrentate the directory according to the extension of the file extension which need to sort given manuannly  
import os
import time
import sys 
import shutil
# in this function we are just appending the extensions of the files in one folder 
# so we get an idea about how much folders we are need to make 
def Find_all_Extensions(Dirname):
    try:
        extensions=[]
        flag=os.path.isabs(Dirname)
        if flag==False:
            Dirname=os.path.abspath(Dirname)
        
        if os.path.exists(Dirname):
                for foldername, subfoldername, filename in os.walk(Dirname):
                    for name in filename:
                        exte=os.path.splitext(name)[1] # this will split the file name in two parts one is name and another one is extension
                        if exte not in extensions:
                            extensions.append(exte)
        return extensions
    except Exception as e:
        print("Error at finding all extensions")
        print(e)
# this function is only to find the name of the file and send to another function whic will move or copy the files  
def Directory_sorter(Dirname):
    try:
        exxt=Find_all_Extensions(Dirname)
        File_copy=[]
        flag=os.path.isabs(Dirname)
        if flag==False:
            Dirname=os.path.abspath(Dirname)
        
        if os.path.exists(Dirname):
            for i in exxt:   # this will iterate over the extensions 
                extension=i   
                for foldername, subfoldername, filename in os.walk(Dirname): # walk method travel through the directory and give name of the files to the another function whos move the files
                    for name in filename:
                        if name.endswith(extension):
                            new_Folder(foldername,extension,name)
    
    except Exception as obj:
        print("Error at sorter")
        print(obj)
# this is the main or back bone of the script  
def new_Folder(foldername,extension,fname):
    try:
        ext=extension
        new_path=os.path.join(foldername,ext)
        if not os.path.exists(new_path):  #check whether the directory exists or not if not then create one else add the file in older directory  
            os.makedirs(new_path,exist_ok=True)
        
        src = os.path.join(foldername, fname)
        dest = os.path.join(new_path, fname)
        shutil.move(src, dest)
        print(fname+" has been moved to the new folder New")

    except Exception as obj:
        print('2')
        print(obj)

def main():
    print("---------------- Directory Sorter -------------------")
    print(sys.orig_argv)
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to perform Directory sort operations")
            exit()

        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of the script : ")
            print("Name_Of_File eg.[temp.py]  Name_Of_Directory [path in whin file is store]  Extentipon_Of_File [Extension of the file which you need to sort]")
            exit()

    if(len(sys.argv) == 2):
        try:
            starttime = time.time()
            Directory_sorter(sys.argv[1])
            endtime = time.time()

            print("Time required to execute the script is : ",endtime-starttime)

        except Exception as obj2:
            print("Unable to perform the task due to ", obj2)
            
    else:
        print("Invalid option")
        print("Use --h option to get the help and use --u option to get the usage of application")
        exit()
    
    print("--------- Thank you for using our script -------------")

if __name__=="__main__":
    main() 