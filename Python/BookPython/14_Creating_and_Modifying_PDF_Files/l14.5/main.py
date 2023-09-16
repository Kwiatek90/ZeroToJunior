from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = Path(r"D:\Programowanie\ZeroToJunior\Python\BookPython\14_Creating_and_Modifying_PDF_Files\l14.5\ugly.pdf")

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

for n in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(n)
    if n % 2 == 0:
        page.rotateClockwise(90)
    pdf_writer.addPage(page)
    
    
with Path("ugly_rotared.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)