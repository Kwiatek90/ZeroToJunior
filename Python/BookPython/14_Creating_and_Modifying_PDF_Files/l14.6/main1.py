from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = Path(r"D:\Programowanie\ZeroToJunior\Python\BookPython\14_Creating_and_Modifying_PDF_Files\l14.6\newsletter_protected.pdf")
pdf_reader = PdfFileReader(str(pdf_path))
pdf_reader.decrypt(password="SuperSecret")

print( pdf_reader.getPage(0))