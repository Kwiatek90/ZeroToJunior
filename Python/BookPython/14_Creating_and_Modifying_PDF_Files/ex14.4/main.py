#1. In the Chapter 14 Practice Files directory there are three PDFs
#called merge1.pdf, merge2.pdf, and merge3.pdf. Using a PdfFileMerger
#instance, concatenate the two files merge1.pdf and merge2.pdf using
#.append().
##in your home directory.

#2. With a new PdfFileMerger instance, use .merge() to merge the file
#merge3.pdf in-between the two pages in the concatenated.pdf file
#you made in exercise 1. Save the new file to your home directory
#as merged.pdf.


#The final result should be a PDF with three pages. The first
#page should have the number 1 on it, the second should have 2,
#and the third should have 3.\
    
from pathlib import Path
from PyPDF2 import PdfFileMerger

merge1_path = r"D:\Programowanie\ZeroToJunior\Python\BookPython\14_Creating_and_Modifying_PDF_Files\ex14.4\merge1.pdf"
merge2_path = r"D:\Programowanie\ZeroToJunior\Python\BookPython\14_Creating_and_Modifying_PDF_Files\ex14.4\merge2.pdf"
merge3_path = r"D:\Programowanie\ZeroToJunior\Python\BookPython\14_Creating_and_Modifying_PDF_Files\ex14.4\merge3.pdf"

pdf_merger = PdfFileMerger()

pdf_merger.append(str(merge1_path))
pdf_merger.append(str(merge2_path))

with Path("concatenated.pdf").open(mode="wb") as output_file:
    pdf_merger.write(output_file)
    
pdf_merger = PdfFileMerger()

pdf_merger.append(str(merge1_path))
pdf_merger.append(str(merge2_path))
pdf_merger.merge(1, str(merge3_path))

with Path("merged.pdf").open(mode="wb") as output_file:
    pdf_merger.write(output_file)