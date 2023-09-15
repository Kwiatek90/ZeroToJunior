from PyPDF2 import PdfFileMerger
from pathlib import Path

reports_dir = r"D:\Programowanie\ZeroToJunior\Python\BookPython\14_Creating_and_Modifying_PDF_Files\l14.4\expense_reports"
reports_dir = Path(reports_dir)

#sorotwanie wedlug kolejnosci
expense_reports = list(reports_dir.glob("*.pdf"))
expense_reports.sort()

pdf_merger = PdfFileMerger()

for path in expense_reports:
    pdf_merger.append(str(path))
    
with Path("expense_reports.pdf").open(mode="wb") as output_file:
    pdf_merger.write(output_file)

