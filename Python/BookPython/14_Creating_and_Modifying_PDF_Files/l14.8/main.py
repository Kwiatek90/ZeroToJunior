from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch, cm
from reportlab.lib.pagesizes import letter, A4

#8,5 inch * 72 points is 612
canvas = Canvas("hello.pdf", pagesize=A4)

canvas.setFont("Times-Roman", 18)
canvas.setFillColor("Blue")
canvas.drawString(2 * cm, 2 * cm, "hello world")
canvas.save()

