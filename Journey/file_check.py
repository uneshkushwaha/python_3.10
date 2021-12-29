# checking if file exists or not by three ways 
   #1.Exception Handling
       #1.IO Error,
       #2.FileNotFoundError

   #2. OS Module
     #it interacts with operating system of the computer  
       #1.   os.path.isfile()
       #2.  os.path.isdir()
       #3.  os.path.exists()
       #returns boolean value

   #3. Pathlib Module
   #it interacts with file system of the computer
       #1.  pathlib.Path.is_file()
       #2.  pathlib.Path.is_dir()
       #3.  pathlib.Path.exists()
           #returns boolean value
import os
path_name = "sagun_diet.txt"
if os.path.isfile(path_name):

  print("File exists")
else:
  print("File does not exist! IOError has occured")


import os
path_name="Doc"
if os.path.isdir(path_name):
    #it checks the directory as a folder
  print("File exists")
else:
  print("File does not exist! IOError has occured")
 

import os
path_name="\python3,10\Doc\sagun_diet.txt"
if os.path.exists(path_name):
      #it checks the mentioned path
  print("File exists")
else:
  print("File does not exist! IOError has occured")



      # Pathlib Module
from pathlib import Path
path_name="Unesh_diet.txt"
p=Path(path_name)
print(p.is_file())

from pathlib import Path
path_name="Doc"
p=Path(path_name)
print(p.is_dir())

from pathlib import Path
path_name="\python3,10\Doc\sagun_diet.txt"
#path_name="\python3,10\Doc"
p=Path(path_name)
print(p.exists()) 