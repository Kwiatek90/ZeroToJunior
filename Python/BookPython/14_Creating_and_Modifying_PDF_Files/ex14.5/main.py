#1. In the Chapter 14 Practice Files folder there is a PDF called
#split_and_rotate.pdf. Create a new PDF called rotated.pdf in
#your home directory containing the pages of split_and_rotate.pdf
#rotated counterclockwise 90 degrees.


#2. Using the rotated.pdf file you created in exercise 1, split each page
#of the PDF vertically in the middle. Create a new PDF called
#split.pdf in your home directory containing all of the split pages.
#split.pdf should have four pages with the numbers 1, 2, 3,
#and 4, in order.

from pathlib import Path
from PyPDF2 import PdfFileWriter, PdfFileReader

pdf_path = Path(r"D:\Programowanie\ZeroToJunior\Python\BookPython\14_Creating_and_Modifying_PDF_Files\ex14.5\split_and_rotate.pdf")

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

for page in pdf_reader.pages:
    page.rotateClockwise(-90)
    pdf_writer.addPage(page)
    
with Path("rotated.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
