import pandas as pd
import os
import PyPDF2

#Create empty txt files Named as pdf files 

path = '~/Downloads/'
newpath = '~/'

# r=root, d=directories, f = files

files = []
for r, d, f in os.walk(path):
    for file in f:
        if '.pdf' in file:
            files.append(os.path.join(r, file))

for f in files:

    txt = f.replace('.pdf','.txt')
    txtpath = txt.replace(path,newpath) 
    print(f)
    ft= open(txtpath ,"w+")
    ft.close()
    print(txtpath)
    Vpath = f.replace('.pdf','')
    # print(Vpath)

    myPDFFile = PyPDF2.PdfFileReader(f)
    with open(txtpath, 'w') as pdf_output:   #, encoding="utf-8"
         for page in range (myPDFFile.getNumPages()):
            data = myPDFFile.getPage(page).extractText()
            pdf_output.write(data)            
    with open(txtpath, 'r') as myPDFContent:
        myPDFContent.read().replace('\n',' ')
