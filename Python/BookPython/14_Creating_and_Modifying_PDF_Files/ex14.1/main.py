#1.In the Chapter 14 Practice Files directory there is a PDF file called
#zen.pdf. Create a PdfFileReader from this PDF.
from PyPDF2 import PdfFileReader
from pathlib import Path

pdf_path = r"D:\Programowanie\ZeroToJunior\Python\BookPython\14_Creating_and_Modifying_PDF_Files\ex14.1\zen.pdf"

pdf = PdfFileReader(str(pdf_path))

#2. Using the PdfFileReader instance from Exercise 1, print the total
#number of pages in the PDF.

print(pdf.getNumPages())

#3. Print the text from the first page of the PDF in Exercise 1.

first_page = pdf.getPage(0)

print(first_page.extractText())