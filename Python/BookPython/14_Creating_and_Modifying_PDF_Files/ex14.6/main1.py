from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = Path(r"D:\Programowanie\ZeroToJunior\Python\BookPython\14_Creating_and_Modifying_PDF_Files\ex14.6\top_secret_encrypted.pdf")

pdf_reader = PdfFileReader(str(pdf_path))

pdf_reader.decrypt(password="Unguessable")

first_page = pdf_reader.getPage(0)

print(first_page.extractText())

