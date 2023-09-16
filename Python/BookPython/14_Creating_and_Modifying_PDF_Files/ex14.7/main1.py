from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = Path(r"Python/BookPython/14_Creating_and_Modifying_PDF_Files/ex14.7/rotate_scrambled.pdf")

def get_page_text(page):
    return page.extractText()

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

pages = list(pdf_reader.pages)

pages.sort(key=get_page_text)

for page in pages:
    pdf_writer.addPage(page)
    
with Path("unscrambled.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)



    