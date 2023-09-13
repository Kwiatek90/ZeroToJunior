from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = r"D:\Programowanie\ZeroToJunior\Python\BookPython\14_Creating_and_Modifying_PDF_Files\l14.1\Pride_and_Prejudice.pdf"

input_pdf = PdfFileReader(str(pdf_path))

first_page = input_pdf.getPage(0)

pdf_writer = PdfFileWriter()
pdf_writer.addPage(first_page)


with Path("first_page.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
    