#Create a class called PdfFileSplitter that reads a PDF from an existing
#PdfFileReader instance and splits the PDF into two new PDFs.
#The class should be instantiated with a path string. For example,
#here’s how you would create a PdfFileSplitter instance from a PDF
#called mydoc.pdf in your current working directory:
#pdf_splitter = PdfFileSplitter("mydoc.pdf")
#The PdfFileSplitter class should have two methods:


#1. .split() that has a single parameter breakpoint that expects an
#integer representing the page number to split the PDF.
#After .split() is called, the PdfFileSplitter class should have
#an attribute .writer1 assigned to a PdfFileWriter instance containing all the pages in the original PDF up to but not including the
#breakpoint page, and .writer2 assigned to a PdfFileWriter instance
#containing the remaining pages in the original PDF.


#2. .write() that has a single parameter filename that expects a path
#string.
#When .write() is called, two PDFs should be written to the
##specified path. The first one with the name filename + "_1.pdf"
#and the second with the name filename + "_2.pdf".
#For example, here’s how you would split the mydoc.pdf at page four:
#pdf_splitter.split(breakpoint=4)
#Then, to write two new PDFs in the current working directory as
#mydoc_split_1.pdf and mydoc_split_2.pdf, you would call .write() with
#the file name "mydoc_split":
#pdf_splitter.write("mydoc_split")
#Check that the splitter works by splitting the Pride_and_Prejudice.pdf
#file in the Chapter 14 Practice Files folder with the breakpoint at the
#150th page.
from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

class PdfFileSplitter:
    def __init__(self, path):
        self.path = path
        self.writer1 = PdfFileWriter()
        self.writer2 = PdfFileWriter()
        
    def split(self, breakpoint):
        input_pdf = PdfFileReader(str(self.path))
        pages = input_pdf.getNumPages()
        print(f"PDF zawiera: {pages}")
    
        for n in range(0, breakpoint):
            page = input_pdf.getPage(n)
            self.writer1.addPage(page)
        
        for n in range(breakpoint, pages):
            page = input_pdf.getPage(n)
            self.writer2.addPage(page)

    def write(self, filename):
        file1 = filename + "_1.pdf"
        file2 = filename + "_2.pdf"
        with Path(file1).open(mode="wb") as output_file:
            self.writer1.write(output_file)
            
        with Path(file2).open(mode="wb") as output_file:
            self.writer2.write(output_file)


    
    
    
pdf_path = r"D:\Programowanie\ZeroToJunior\Python\BookPython\14_Creating_and_Modifying_PDF_Files\l14.1\Pride_and_Prejudice.pdf"

pdf_splitter = PdfFileSplitter(pdf_path)

pdf_splitter.split(10)
pdf_splitter.write("test")
