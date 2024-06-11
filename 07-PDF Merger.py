#Merge PDF
from PyPDF2 import PdfMerger
from os import listdir

merger = PdfMerger()
path=listdir('')
pdf=[]
for i in range(len(path)):
    if path[i].endswith('.pdf'):
        pdf.append(path[i])

for pdf_file in pdf:
    merger.append(pdf_file)

merger.write("merged_pages.pdf")
merger.close()
            
