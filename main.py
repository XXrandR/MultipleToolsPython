import PyPDF2

path = '/home/cisco/Downloads/Leader.pdf'
newpath = '/home/cisco/result.txt'

reader = PyPDF2.PdfReader(path)
pag = 0

f = open(newpath, "w")
while pag < len(reader.pages):
    page = reader.pages[pag]
    pag+=1;
    print("Page: ", pag)
    a = page.extract_text()
    print(a)
    f.write(a)
f.close()
