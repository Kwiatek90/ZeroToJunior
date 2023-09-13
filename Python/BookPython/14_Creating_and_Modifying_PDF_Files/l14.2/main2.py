from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = r"D:\Programowanie\ZeroToJunior\Python\BookPython\14_Creating_and_Modifying_PDF_Files\l14.1\Pride_and_Prejudice.pdf"

input_pdf = PdfFileReader(str(pdf_path))

pdf_writer = PdfFileWriter()
for n in range(1,4):
    page = input_pdf.getPage(n)
    pdf_writer.addPage(page)
    
with Path("chapter1.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
