import fitz

# Define paths to the PDF and XML files
pdf_file_path = r'/mnt/D/Upwork/trials/Draw_pdf_invoice/invoice-intelli test.pdf'
xml_file_path = r'/mnt/D/Upwork/trials/Draw_pdf_invoice/invoice.xml'
output_file_path = r'/mnt/D/Upwork/trials/Draw_pdf_invoice/invoice-intelli embedded xml.pdf'

def embed_xml(pdf_file_path, xml_file_path, output_file_path):
    # Open the PDF file
    pdf_doc = fitz.open(pdf_file_path)

    # Read the contents of the XML file
    with open(xml_file_path, 'rb') as xml_file:
        xml_data = xml_file.read()

    # Embed the XML data as an annotation in the first page of the PDF
    page = pdf_doc[0]
    pdf_doc.embfile_add("XML file",xml_data,"invoice.xml")

    # Save the PDF file with the embedded XML data
    pdf_doc.save(output_file_path)

embed_xml(pdf_file_path, xml_file_path, output_file_path)
