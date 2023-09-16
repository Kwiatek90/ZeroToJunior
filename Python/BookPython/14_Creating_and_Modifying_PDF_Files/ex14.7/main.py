#In the Chapter 14 Practice Files folder there is a PDF file called
#scrambled.pdf with seven pages. Each page contains a number 1
#through 7, but they are out of order.
#Additionally, some of the pages are rotated by one of 90, 180, or 270
#degrees in either the clockwise or counterclockwise position.
#Write a script that unscrambles the PDF by sorting the pages according to the number contained in the page text and rotating the page, if
#needed, so that it is upright.
##You can assume that every PageObject read from scrambled.pdf
#has a "/Rotate" key.
#Save the unscrambled PDF to a file called unscrambled.py in your home
#directory.

from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = Path(r"Python/BookPython/14_Creating_and_Modifying_PDF_Files/ex14.7/scrambled.pdf")

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

for page in pdf_reader.pages:
    if page["/Rotate"] == -90:
        page.rotateClockwise(90)
    elif page["/Rotate"] == 90:
        page.rotateClockwise(-90)
    elif page["/Rotate"] == 180:
        page.rotateClockwise(-180)
    elif page["/Rotate"] == -180:
        page.rotateClockwise(180)
    pdf_writer.addPage(page)
    
with Path("rotate_scrambled.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
    
    
