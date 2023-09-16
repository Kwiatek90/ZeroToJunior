from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter
import copy

pdf_path = Path(r"D:\Programowanie\ZeroToJunior\Python\BookPython\14_Creating_and_Modifying_PDF_Files\l14.5\half_and_half.pdf")

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

first_page = pdf_reader.getPage(0)

#lewy wycinek strony
left_side = copy.deepcopy(first_page)
current_cords = left_side.mediaBox.upperRight
new_coords = ( current_cords[0] / 2, current_cords[1])
left_side.mediaBox.upperRight = new_coords

#prawy wycinek strony
right_side = copy.deepcopy(first_page)
right_side.mediaBox.upperLeft = new_coords

#zapis
pdf_writer.addPage(left_side)
pdf_writer.addPage(right_side)

with Path("cropped_pages.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
