import PyPDF2

#extract text from a PDF file

pdfFile = open('Automation\\files\\meetmin1.pdf', 'rb') # pdf are binary so need to specify read binary
reader = PyPDF2.PdfFileReader(pdfFile)

print(reader.numPages)

page = reader.getPage(0)
print(page.extractText())

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText())
    
pdfFile.close()

#join two pdfs into a single pdf

pdfFile1 = open('Automation\\files\\meetmin1.pdf', 'rb') #
pdfFile2 = open('Automation\\files\\meetmin2.pdf', 'rb')

reader1 = PyPDF2.PdfFileReader(pdfFile1)
reader2 = PyPDF2.PdfFileReader(pdfFile2)

writer = PyPDF2.PdfFileWriter()

for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)
    
for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)
    
newPDF = open('Automation\\files\\meetmin3.pdf', 'wb') # pdf are binary so need to specify write binary
writer.write(newPDF)

pdfFile1.close()
pdfFile2.close()