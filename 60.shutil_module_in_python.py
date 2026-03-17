#shutil() is a built in function in python
#now we use shutil.copy("src","dic")
#it copy the data of src file to dic file
import shutil
import os
# shutil.copy("59.walrus operator.py","rahulbhuyan.py") #here copy the all data of walrus operator and transfer into rahulbhuyan.py files
# os.remove("rahulbhuyan.py") #here remove the files but it cannot remove files by using shutil function, so we use OS module
#__________________________________________________________________
#shutil.copy2("src","dic")
#it copy and transfer more data from original file to new file
# shutil.copy2("57.hybrid inheritance.py","rahulkumar.py")
# os.remove("rahulkumar.py")
#___________________________________________________________________
#shutil.copytree("src","dsc"):
#this function recursively copies the directory to new directory. if the destination location is already exists then the original directory
#merged with it 
# shutil.copytree("practice programes.py","habit programes.py")
#now we want to remove the new generate directory "habit programes.py"
# shutil.rmtree("habit programes.py") 
#______________________________________________________________________
# shutil.move("folder_name/file.py","newfolder") now the file.py move to the newfolder location 

#____________________________________________________________________________
""" 
import shutil
shutil.make_archive("name","zip","my folder") in this case name.zip file created in my folder
___________________________________________________________________________________

import shutil
shutil.unpack_archive("name.zip","extracted_folder")
____________________________________________________________________________________

import shutil
total,used,free=shutil.disk_usage("/")
print("Total : ", total)
print("Used : ",used)
print("Free: ",free)
 isme disk a total,used aur free space batadeta hai
"""
