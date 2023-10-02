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

input_path = gui.fileopenbox(title="Select PDF to extract page..", default="*.pdf")

if input_path is None:
    exit()
    
start_page = gui.enterbox(msg="Choose starting page number ...", title="Starting page")
if start_page is None:
    exit()
    
while start_page < 0:
    gui.msgbox(msg="You put wrong number!", title="Wrong number")
    start_page = gui.enterbox(msg="Choose starting page number ...", title="Starting page")
    
#trzeba ustaic zeby nie przepuszczalo stringa

