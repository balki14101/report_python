from fpdf import FPDF

from json_pdf_generator import user_details,final_recommendations

#generate pdf 
def create_pdf(content_dict, filename):
    # Create instance of FPDF class
    pdf = FPDF()
    
    
# Page 1: General Information
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Survey Header", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Username: {user_details["Name"]}, Age: {user_details["Age"]}", ln=True, align="L")
    pdf.ln(10)

# Page 2: Domain Percentage with Pie Chart
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Percentage of Correct Answers by Domain", ln=True, align="C")
    pdf.ln(10)
    pdf.image("domain_barchart.png", x=45, y=20, w=120)


# Page 3: Subdomain Percentage with Pie Chart
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Percentage of Correct Answers by Subdomain", ln=True, align="C")
    pdf.ln(10)
    pdf.image("subdomain_barchart.png", x=45, y=20, w=120)

    
# Page 4: recommendation
    pdf.add_page()
    pdf.set_font("Arial", style='B',size=16)
    pdf.cell(200, 10, txt="Survey Report", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", size=12)

    for title, text in content_dict.items():
        pdf.cell(200, 6, txt=title, ln=True)
        pdf.multi_cell(0, 6, txt=text)
        pdf.ln(5)
    
    # Save the PDF to a file
    pdf.output(filename)


create_pdf(final_recommendations, "final_survey_report.pdf")
