import zipfile

f = zipfile.ZipFile("suhan.zip",'w')

f.write("suhan2.py")

f.close()