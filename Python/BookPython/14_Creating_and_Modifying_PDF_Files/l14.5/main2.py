from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = Path(r"D:\Programowanie\ZeroToJunior\Python\BookPython\14_Creating_and_Modifying_PDF_Files\l14.5\half_and_half.pdf")

pdf_reader = PdfFileReader(str(pdf_path))
first_page = pdf_reader.getPage(0)

first_page.mediaBox.upperLeft = (0,480)

pdf_writer = PdfFileWriter()
pdf_writer.addPage(first_page)

with Path("cropped_page.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)