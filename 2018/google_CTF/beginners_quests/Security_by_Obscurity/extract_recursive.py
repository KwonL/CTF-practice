import zipfile
import os
import lzma

count = 1

zf = zipfile.ZipFile('security.zip') 
zf.extractall(path='./1/') 

while True :
    path = os.listdir('./' + str(count) + '/')[0]

    # zip 
    if count < 17 : 
        try :
            zf = zipfile.ZipFile('./' + str(count) + '/' + path)
            count += 1
            zf.extractall(path='./' + str(count) + '/')
            print("Extract count : " + str(count))
        except Exception as e :
            print(e)
            print("Stopped: " + str(count))
            break

    # xz
    else :
        try :
            
