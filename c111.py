import os
import shutil

#print(dir(os))
path=os.getcwd()
print("The path of the file is ",path)

#os.mkdir("102")

result=os.listdir("C:/Users/asus/OneDrive/Desktop")
print(result)

path1=os.path.exists("C:/Users/asus/OneDrive/Desktop")
print(path1)





destination="C:/Users/asus/Downloads"
source="C:/Users/asus/OneDrive/Desktop_abc"
files=os.listdir(source)
print(files)
for i in files:
    name,ext=os.path.splitext(i)
    print("The name of the file is",name)
    print("The ext of the file is",ext)
    
abc=shutil.move(source,destination)