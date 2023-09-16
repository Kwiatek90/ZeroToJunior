from pathlib import Path
from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_path = Path(r"D:\Programowanie\ZeroToJunior\Python\BookPython\14_Creating_and_Modifying_PDF_Files\l14.6\newsletter.pdf")

pdf_reader = PdfFileReader(str(pdf_path))
pdf_writer = PdfFileWriter()


pdf_writer.appendPagesFromReader(pdf_reader)

pdf_writer.encrypt(user_pwd="SuperSecret")

with Path("newsletter_protected.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)