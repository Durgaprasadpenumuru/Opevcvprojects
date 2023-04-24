"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists
"""
#the below line creates a file with namedemofile
f = open("demofile.txt", "w")
#the below line reads the contents of file when it is in r mode
f = open("demofile.txt", "r")
print(f.read())
#If the file is located in a different location, you will have to specify the file path, like this:
"""
f = open("D:\\myfiles\welcome.txt", "r")
print(f.read())
"""
#Loop through the file line by line:
f = open("demofile.txt", "r")
for x in f:
  print(x)
#afterreadingthefileneedtocloseit lik the below lines
f = open("demofile.txt", "r")
print(f.readline())
f.close()
#Write to an Existing File, a will append and w will overwrite the existing data
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())
#deleting the file using the below line
import os
os.remove("demofile.txt")
#Check if File exist:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
#Delete Folder, can only empty the folders not the folder itself
import os
if os.path.exists("myfolder"):
  os.rmdir("myfolder")
#with syntax for file handling
with open("hello.txt", "w") as my_file:
  my_file.write("Hello world \n")
  my_file.write("I hope you're doing well today \n")
  my_file.write("This is a text file \n")
  my_file.write("Have a nice time \n")

with open("hello.txt") as my_file:
  for line in my_file:
    print(line)
