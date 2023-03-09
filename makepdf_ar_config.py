# Importing Required Module
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import arabic_reshaper
from bidi.algorithm import get_display


path = r'/mnt/D/Upwork/trials/Draw_pdf_invoice/'

c = canvas.Canvas(f"{path}invoice-intelli.pdf",pagesize=(2480,3508),bottomup=0)

# Registering Arabic Font
pdfmetrics.registerFont(TTFont('KacstL', f'{path}KacstLetter.ttf'))

# Setting and reshaping Arabic text
c.setFont('KacstL', 80)
text = u'فاتورة ضريبية'
ar = arabic_reshaper.reshape(text)
ar = get_display(ar)
# Inserting the name of the company
c.drawCentredString(2000,560,ar)


# End the Page and Start with new
c.showPage()

# Saving the PDF
c.save()