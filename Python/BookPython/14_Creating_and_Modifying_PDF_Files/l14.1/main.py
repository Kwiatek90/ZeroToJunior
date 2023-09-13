from PyPDF2 import PdfFileReader    
from pathlib import Path

pdf_path = r"D:\Programowanie\ZeroToJunior\Python\BookPython\14_Creating_and_Modifying_PDF_Files\l14.1\Pride_and_Prejudice.pdf"

pdf = PdfFileReader(str(pdf_path))

print(pdf.getNumPages())
print(pdf.documentInfo.title)

first_page = pdf.getPage(0)
file_path = r"D:\Programowanie\ZeroToJunior\Python\BookPython\14_Creating_and_Modifying_PDF_Files\l14.1\text.txt"

#zapiswanie pdf od plik tekstowego

#with open(file_path, mode="w", encoding="utf-8") as file:
#    writer = file.write(first_page.extractText())
