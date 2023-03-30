import PyPDF2, os


# Change directory of program
os.chdir('/home/tabish/Documents/LEARN_PYTHON/additional material for Automate the boring stuff/')


# Get all files in directory and sort alphabetically
dirFiles = os.listdir()
dirFiles.sort()


# Initiate empty list and append pdf file names
desFiles = []
for i in dirFiles:
    if i.endswith('.pdf'):
        desFiles.append(i)
        

pdfWriter = PyPDF2.PdfFileWriter()

for i in desFiles:
    pdfFile = open(i,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    if pdfReader.isEncrypted == True:
        ans = input('Enter password: ') # << password here
        pdfReader.decrypt(ans)
        if pdfReader.numPages < 2:
            for j in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(j)
                pdfWriter.addPage(pageObj)
        else:
            for j in range(1,pdfReader.numPages):
                pageObj = pdfReader.getPage(j)
                pdfWriter.addPage(pageObj)
    else:
        if pdfReader.numPages < 2:
            for j in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(j)
                pdfWriter.addPage(pageObj)
        else:
            for j in range(1,pdfReader.numPages):
                pageObj = pdfReader.getPage(j)
                pdfWriter.addPage(pageObj)

        
os.chdir('/home/tabish/Documents/LEARN_PYTHON/PyProjects/')
pdfOutF = open('allminutes.pdf', 'wb')
pdfWriter.write(pdfOutF)
pdfOutF.close()
