from fpdf import FPDF

from PIL import Image

from data import page_style


# create a pdf object
pdf = FPDF()
pdf.add_page()

# add text
pdf.set_font('Arial', 'B', 16)
# pdf.cell(40, 10, 'myndwell', 0, 2, 'C')
pdf.set_font('Arial', 'B', 14)
pdf.cell(200, 40, 'Survey Report', 0, 2, 'C')

# add image
pdf.image('logo.png', 10, 10, 30)

# add a line
pdf.line(10, 40, 200, 40)

# add text
pdf.set_font('Arial', '', 12)
pdf.cell(40, 10, 'Person Name: John Doe', 0, 2)
pdf.cell(40, 10, 'Survey Title: Mental Health', 0, 2)
pdf.cell(40, 10, 'Date: 30/01/2024', 0, 2)

pdf.set_font('Arial', 'B', 14)
pdf.cell(40, 10, 'About this Survey', 0, 2)
# add a multi-line text
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 5, 'A psychology survey is a research tool used to gather information about various psychological phenomena, attitudes, behaviors, or experiences of individuals. These surveys are designed to explore a wide range of topics within psychology, including personality traits, mental health issues, cognitive processes, social interactions, and more.\n\nTypically, psychology surveys consist of a series of rating scales or open-ended questions. The questions are often crafted to address specific research objectives and hypotheses, and they may cover various aspects of the human mind and behavior.')

# add an image
# pdf.image('placeholder_image.jpg', 10, 100, 100)

# add text
pdf.set_font('Arial', 'B', 14)
pdf.cell(40, 10, 'Is this survey accurate?', 0, 2)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 5, 'Claiming 100% accuracy for any survey is unrealistic. While surveys aim for accuracy, inherent limitations such as response bias or sampling errors prevent absolute certainty. Acknowledging these limitations fosters transparency and credibility in research. Thus, while striving for accuracy, claiming 100% accuracy is not feasible.')

# add a table
pdf.add_page()
pdf.set_font('Arial', 'B', 12)
pdf.cell(40, 10, 'Score: 55', 0, 2)
pdf.cell(40, 10, 'Level: Moderate', 0, 2)
pdf.cell(40, 10, 'Diff: Ranges', 0, 2)
# pdf.line(10, 180, 200, 180)
pdf.set_font('Arial', '', 10)
pdf.cell(40, 10, 'Normal (0-30)', 1, 0)
pdf.cell(40, 10, 'Moderate (31-70)', 0, 0)
pdf.cell(40, 10, 'Severe (70-100)', 0, 0)
# pdf.cell(40, 10, 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.', 0, 0)
# pdf.cell(40, 10, 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.', 0, 0)
# pdf.cell(40, 10, 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.', 0, 2)

pdf.ln()



# add text
pdf.set_font('Arial', 'B', 14)
pdf.cell(40, 10, 'Score Analysis', 0, 2)
# Add text "Domain Analysis"
pdf.set_font('Arial', 'B', 12)
pdf.cell(40, 10, 'Domain Analysis', 0, 2)  # Move to the next line after the cell

# Add chart for domain analysis
pdf.image('domain_barchart.png', 10, None, 100)  # Move to the next line after the image

# Add text "Sub-Domain Analysis"
pdf.set_font('Arial', 'B', 12)
pdf.cell(40, 10, 'Sub-Domain Analysis', 0, 2)  # Move to the next line after the cell

# Add chart for sub-domain analysis
pdf.image('subdomain_barchart.png', 10, None, 100)  

# add text
pdf.set_font('Arial', 'B', 14)
pdf.cell(40, 10, 'Recommandation', 0, 2)
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 5, 'It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.\n\nThe point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using \'Content here, content here\', making it look like readable English.')


# add a footer
# pdf.set_y(-15)
# pdf.set_font('Arial', 'I', 8)
# pdf.cell(0, 10, 'Page %s' % pdf.page_no(), 0, 0, 'C')

# output the pdf
pdf.output('survey_report.pdf')

# #read your PDF
# with open("survey_report.pdf", "rb") as f:
#     pdf = PyPDF2.PdfFileReader(f)
#     page = pdf.getPage(0)
#     pdf_writer = PyPDF2.PdfFileWriter()
#     pdf_writer.addPage(page)

#     #add an image as watermark
#     watermark = Image.open("watermark.png")
#     watermark_width, watermark_height = watermark.size
#     page_width, page_height = page.mediaBox.upperRight
#     watermark_ratio = watermark_width / watermark_height
#     watermark_width = page_width * 0.2
#     watermark_height = watermark_width / watermark_ratio
#     x = (page_width - watermark_width) / 2
#     y = (page_height - watermark_height) / 2
#     watermark = watermark.resize((int(watermark_width), int(watermark_height)))
#     watermark.putalpha(128)
#     page.mergePage(watermark)

#     #write the watermarked pdf
#     with open("survey_report_watermarked.pdf", "wb") as output_file:
#         pdf_writer.write(output_file)