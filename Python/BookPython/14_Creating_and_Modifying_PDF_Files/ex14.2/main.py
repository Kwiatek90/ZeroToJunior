#1. Extract the last page from the Pride_and_Prejudice.pdf file and save
#it to a new file called last_page.pdf in your home directory.
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = r"D:\Programowanie\ZeroToJunior\Python\BookPython\14_Creating_and_Modifying_PDF_Files\l14.1\Pride_and_Prejudice.pdf"

input_pdf = PdfFileReader(str(pdf_path))
last_page = input_pdf.getPage(233)

pdf_writer = PdfFileWriter()
pdf_writer.addPage(last_page)

with Path("last_page.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)


#2. Extract all pages with even numbered indices from the Pride_-
#and_Prejudice.pdf and save them to a new file called every_other_-
#page.pdf in your home directory.

pdf_writer1 = PdfFileWriter()
for n in range(1,233):
    if n % 2 == 0:
        page = input_pdf.getPage(n)
        pdf_writer1.addPage(page)

with Path("ever_other_page.pdf").open(mode="wb") as output_file:
    pdf_writer1.write(output_file)

#3. Split the Pride_and_Prejudice.pdf file into two new PDF files. The
#first file should contain the first 150 pages, and the second file
#should contain the remaining pages. Save both files in your home
#directory as part_1.pdf and part_2.pdf.

pdf_writer2 = PdfFileWriter()
for n in range(0,150):
    page = input_pdf.getPage(n)
    pdf_writer2.addPage(page)
    
with Path("part_1.pdf").open(mode="wb") as output_file:
    pdf_writer2.write(output_file)
   
pdf_writer3 = PdfFileWriter()    
for n in range(150,234):
    page = input_pdf.getPage(n)
    pdf_writer3.addPage(page)
    
with Path("part_2.pdf").open(mode="wb") as output_file:
    pdf_writer3.write(output_file)