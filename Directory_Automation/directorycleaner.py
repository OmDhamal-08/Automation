# this will arrange or just diffrentate the directory according to the extension of the file extension which need to sort given manuannly  
import os
import time
import sys 
import shutil

def Directory_sorter(Dirname,extension):
    try:
        File_copy=[]
        flag=os.path.isabs(Dirname)
        if flag==False:
            Dirname=os.path.abspath(Dirname)
        
        if os.path.exists(Dirname):
                for foldername, subfoldername, filename in os.walk(Dirname):
                    for name in filename:
                        if name.endswith(extension):
                            new_Folder(foldername,extension,name)
    
    except Exception as obj:
        print("Error at sorter")
        print(obj)

def new_Folder(foldername,extension,fname):
    try:
        ext=extension
        new_path=os.path.join(foldername,ext)
        os.makedirs(new_path,exist_ok=True)
        
        src = os.path.join(foldername, fname)
        dest = os.path.join(new_path, fname)
        shutil.copyfile(src, dest)
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

    if(len(sys.argv) == 3):
        try:
            starttime = time.time()
            Directory_sorter(sys.argv[1],sys.argv[2])
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