# Importing Required Module
from reportlab.pdfgen import canvas

path = r'/mnt/D/Upwork/trials/Draw_pdf_invoice/'
res_path = r'/mnt/D/Upwork/trials/Draw_pdf_invoice/resources/'
# Creating Canvas
c = canvas.Canvas(f"{path}invoice-intelli.pdf",pagesize=(2480,3508),bottomup=0)

# Logo Section
# Setting th origin to (10,40)
c.translate(1820,700)
c.scale(1,-1)

c.drawImage(f"{res_path}intelli-logo.jpg",0,0,width=400,height=400)

c.scale(1,-1)
c.translate(-1820,-700)

# Footer Section
# Setting th origin to (10,40)
c.translate(1474,3520)
c.scale(1,-1)

c.drawImage(f"{res_path}shape.jpg",0,0,width=1006,height=304)

c.scale(1,-1)
c.translate(-1474,-3520)

# Header Section
# Setting the origin back to (0,0) of top-left
c.translate(0,304)
c.scale(1,-1)

c.drawImage(f"{res_path}shape2.jpg",0,0,width=1006,height=304)

c.scale(1,-1)
c.translate(0,-304)

# Body Section
# Setting the origin back to (0,0) of top-left
c.translate(0,1300)
c.scale(1,-1)

c.drawImage(f"{res_path}rect.jpg",0,0,width=2480,height=138)

c.scale(1,-1)
c.translate(0,-1300)

# Total Section
# Setting the origin back to (0,0) of top-left
c.translate(1700,2050)
c.scale(1,-1)

c.drawImage(f"{res_path}rect.jpg",0,0,width=2480,height=138)

c.scale(1,-1)
c.translate(-1700,-2050)


# Payment Section
# Setting the origin back to (0,0) of top-left
c.translate(0,2250)
c.scale(1,-1)

c.drawImage(f"{res_path}rect.jpg",0,0,width=800,height=138)

c.scale(1,-1)
c.translate(0,-2250)


# Title Section
# Setting the font for Name title of company
c.setFont("Helvetica-Bold",80)

# Inserting the name of the company
c.drawCentredString(415,560,"INVOICE")

# Changing the font size for Specifying Address
# c.setFont("Helvetica",70)
# c.setFont("Helvetica-Bold",5)

c.setFont("Helvetica",60)
c.drawString(250,800,"Invoice to")
c.setFont("Helvetica",45)
c.drawString(250,880,"IntelliCare")
c.drawString(250,960,"30 N Gould St, Sheridan, Wyoming, United States")
c.drawString(250,1040,"info@intellicare-assoc.com")

# c.drawString(2000,880,"Invoice No.:")
c.drawString(1830,960,"Invoice No.: 12345")
c.drawString(1830,1040,"Date: 02/02/2023")

# Rect Text
c.setFont("Helvetica-Bold",50)
c.setFillColorRGB(255,255,255)
c.drawString(250,1240,"SN.")
c.drawString(750,1240,"DESCRIPTION")
c.drawString(1500,1240,"QTY")
c.drawString(1760,1240,"UNIT")
c.drawString(2000,1240,"AMOUNT")

# Invoice Items
c.setFont("Helvetica",40)
c.setFillColorRGB(0,0,0)
c.drawString(250,1400,"502")
c.drawString(750,1400,"Optician Visit")
c.drawString(1500,1400,"$50.00")
c.drawString(1800,1400,"1")
c.drawString(2040,1400,"$50.00")

c.drawString(250,1500,"223")
c.drawString(750,1500,"Dentist Visit")
c.drawString(1500,1500,"$70.00")
c.drawString(1800,1500,"1")
c.drawString(2040,1500,"$70.00")

# Total section
c.setFont("Helvetica",50)
c.setFillColorRGB(0,0,0)
c.drawCentredString(2000,1750,"Grand Total: $120.00")
c.drawCentredString(2000,1850,"Tax: $12.00")
c.setFont("Helvetica-Bold",60)
c.setFillColorRGB(255,255,255)
c.drawCentredString(2000,2000,"Total: $132.00")

# Payment Info
# c.setFont("Helvetica",60)

c.setFont("Helvetica-Bold",60)
c.setFillColorRGB(255,255,255)
c.drawString(250,2200,"Payment Info.:")
c.setFont("Helvetica",45)
c.setFillColorRGB(0,0,0)
c.drawString(250,2320,"Account: 123456")
c.drawString(250,2400,"Account Name: IntelliCare")
c.drawString(250,2480,"Bank Details: IntelliCare Details")


# End the Page and Start with new
c.showPage()

# Saving the PDF
c.save()