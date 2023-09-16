from pathlib import Path
from PyPDF2 import PdfFileWriter, PdfFileReader
import copy

pdf_path = Path(r"D:\Programowanie\ZeroToJunior\Python\BookPython\14_Creating_and_Modifying_PDF_Files\ex14.5\rotated.pdf")

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

page = pdf_reader.getPage(0)

print(page.mediaBox)

#dzielimy na pol strone
for page in pdf_reader.pages:
    
    #lewa strona
    left_side = copy.deepcopy(page)
    current_cords = left_side.mediaBox.upperRight
    new_cords= (current_cords[0] / 2, current_cords[1]) 
    left_side.mediaBox.upperRight = new_cords
    
    #lewa stron 
    right_side = copy.deepcopy(page)
    right_side.mediaBox.upperLeft = new_cords 
    
    #dodajemy strony do  instancji
    pdf_writer.addPage(left_side)
    pdf_writer.addPage(right_side)
    
with Path("split.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)
    
    
