from PyPDF2 import PdfFileWriter
from pathlib import Path

pdf_writer = PdfFileWriter()

with Path("blank.pdf").open(mode="wb") as output_file:
    pdf_writer.write(output_file)

