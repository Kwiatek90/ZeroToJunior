 #In the Chapter 14 Practice Files folder there is a PDF file called
#top_secret.pdf. Using PdfFileWriter.encrypt(), encrypt the file with
#the user password Unguessable.
#Save the encrypted file as to your home directory with the
##filename top_secret_encrypted.pdf.
#2. Open the top_secret_encrpyted.pdf file you created in Exercise 1, decrypt it, and print the text contained on the first page of the PD

from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = Path(r"D:\Programowanie\ZeroToJunior\Python\BookPython\14_Creating_and_Modifying_PDF_Files\ex14.6\top_secret.pdf")

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()

pdf_writer.appendPagesFromReader(pdf_reader)
pdf_writer.encrypt(user_pwd="Unguessable")

with Path("top_secret_encrypted.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)


