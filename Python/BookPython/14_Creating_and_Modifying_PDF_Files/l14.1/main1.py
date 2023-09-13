from pathlib import Path
from PyPDF2 import PdfFileReader

pdf_path = r"D:\Programowanie\ZeroToJunior\Python\BookPython\14_Creating_and_Modifying_PDF_Files\l14.1\Pride_and_Prejudice.pdf"
pdf_reader = PdfFileReader(str(pdf_path))

output_file_path = r"D:\Programowanie\ZeroToJunior\Python\BookPython\14_Creating_and_Modifying_PDF_Files\l14.1\Pride_and_Prejudice.txt"

with open(output_file_path, mode="w") as file:
    file.write(
        f"{pdf_reader.documentInfo.title}\n"
        f"Number of pages:{pdf_reader.getNumPages()}\n\n"
    )
    
    #for page in pdf_reader.pages:
    #    text = page.extractText()
    #    file.write(text)
        
        