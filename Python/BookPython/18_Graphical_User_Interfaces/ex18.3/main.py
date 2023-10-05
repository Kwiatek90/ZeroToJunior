#In this challenge, you’ll use EasyGUI to write a GUI application for
#extracting pages from a PDF file.
#Here’s a detailed plan for the application:
#1. Ask the user to select a PDF file to open.
#2. If no PDF file is chosen, exit the program.
#3. Ask for a starting page number.
#4. If the user does not enter a starting page number, exit the program.
#5. Valid page numbers are positive integers. If the user enters an
#invalid page number:
#• Warn the user that the entry is invalid .
#• Return to step 3.
#6. Ask for an ending page number.
#7. If the user does not enter an ending page number, exit the program.
#8. If the user enters an invalid page number:
#• Warn the user that the entry is invalid .
#• Return to step 6.
#9. Ask for the location to save the extracted pages.
#10. If the user does not select a save location, exit the program.
#11. If the chosen save location is the same as the input file path:
#• Warn the user that they can not overwrite the input file.
#• Return to step 9.
#12. Perform the page extraction:
#• Open the input PDF file.
#• Write a new PDF file containing only the pages in the selected
#page range
import easygui as gui
from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

input_path = gui.fileopenbox(title="Select PDF to extract page..", default="*.pdf")

if input_path is None:
    exit()
    
start_page = gui.enterbox(msg="Choose starting page number ...", title="Starting page")
if start_page is None:
    exit()
    
start_page = int(start_page)
    
while start_page < 0:
    gui.msgbox(msg="You put wrong number!", title="Wrong number")
    start_page = gui.enterbox(msg="Choose starting page number ...", title="Starting page")

end_page = gui.enterbox(msg="Choose end page number ...", title="End page")
if end_page is None:
    exit()
    
end_page = int(end_page)
    
while end_page < 0:
    gui.msgbox(msg="You put wrong number!", title="Wrong number")
    end_page = gui.enterbox(msg="Choose end page number ...", title="End page")
    
save_title = "Save the merged PDF as ..."
file_type = "*.pdf"

output_path = gui.filesavebox(title=save_title, default=file_type)

while input_path == output_path:
    gui.msgbox(msg="Cannot overwrite original file!")
    output_path = gui.filesavebox(title=save_title, default=file_type)
    
if output_path is None:
    exit()
    
input_file = PdfFileReader(input_path)
output_pdf = PdfFileWriter()

for n in range(start_page, end_page):
    page = input_file.getPage(n)
    output_pdf.addPage(page)
    
with Path(output_path).open(mode="wb") as output_file:
    output_pdf.write(output_file)


