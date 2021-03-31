import io

from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

def generate_pdf1(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    
    width, height = A4

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
 
        

    p.drawString(100, height - 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')

def generate_pdf2(request):
     # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    data = (
        ("Koksu", "Kulawy"),
        ("Kubuś", "Puchatek"),
        ("Osiołek", "Kłapouchy"),
    )

    doc = SimpleDocTemplate(buffer, pagesize = A4)

    elements = []

    t=Table(data)
    t.setStyle(TableStyle([('BACKGROUND',(1,1),(-2,-2),colors.green),
    ('TEXTCOLOR',(0,0),(1,-1),colors.red)]))
    
    elements.append(t)
    # write the document to disk
    doc.build(elements)    

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello2.pdf')
