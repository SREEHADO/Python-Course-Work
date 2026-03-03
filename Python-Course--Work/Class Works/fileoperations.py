
try:
    file = open('C:/Users/dosap/OneDrive/Desktop/Python Course Work/Python-Course--Work/Class Works\A.txt','r')
except Exception as e:
    print(f"Error Occured: {e}")
else:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.close()

try:
    file = open('C:/Users/dosap/OneDrive/Desktop/Python Course Work/Python-Course--Work/Class Works\A2.txt','a+')
except Exception as e:
    print(f"Error Occured: {e}")
else:
    file.write("/nopening file/nclosing file")
    file.seek(0)
    print(file.read())
    file.close()

with open('C:/Users/dosap/OneDrive/Desktop/Python Course Work/Python-Course--Work/Class Works\A.txt','r') as file:
    print(file.read())

import os

os.mkdir('C:/Users/dosap/OneDrive/Desktop/Python Course Work/Python-Course--Work/Class Works/File Operations/new')

os.makedirs('C:/Users/dosap/OneDrive/Desktop/Python Course Work/Python-Course--Work/Class Works/File Operations/new')

os.rmdir('C:/Users/dosap/OneDrive/Desktop/Python Course Work/Python-Course--Work/Class Works/File Operations/new')

print(os.getcwd)