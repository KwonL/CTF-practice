import zipfile

with open('list.txt', 'r') as f :
    for passwd in f :
        try :
            passwd = passwd.replace('\n', '')
            
            mondai_zip = zipfile.ZipFile('mondai2.zip')
            mondai_zip.extractall(pwd=passwd.encode())
            print(passwd)

            mondai_zip.close()
        except Exception as e :
            pass