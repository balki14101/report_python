import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt

sheet_name="Recommendations"
 # Read the Excel data
#questions sheet
data = pd.read_excel("data1.xlsx")
#recommendation sheet
df = pd.read_excel("data1.xlsx",sheet_name=sheet_name)

# Find unique domain names
domain_names = data["Domain"].unique()

# Find unique subdomain names
sub_domain_names = data["Sub Domain"].unique()

domain_with_percentages = {}
for domain_name in domain_names:
    filtered_data = data[data["Domain"] == domain_name]
    correct_answers = filtered_data["Score"].sum()
    total_questions = len(filtered_data)
    percentage = (correct_answers / total_questions) * 100
    domain_with_percentages[domain_name] = percentage
domain_percentages = list(domain_with_percentages.values())    



sub_domain_with_percentages = {}
for subdomain_name in sub_domain_names:
    filtered_data = data[data["Sub Domain"] == subdomain_name]
    correct_answers = filtered_data["Score"].sum()
    total_questions = len(filtered_data)
    percentage = (correct_answers / total_questions) * 100
    sub_domain_with_percentages[subdomain_name] = percentage
subdomain_percentages = list(sub_domain_with_percentages.values())    

# Generate pie charts
plt.figure(figsize=(10, 6))
plt.pie(domain_percentages, labels=domain_names, autopct='%1.1f%%', startangle=140)
plt.title("Percentage of Correct Answers by Subdomain")
plt.savefig("1.png")
plt.close()    


plt.figure(figsize=(10, 6))
plt.pie(subdomain_percentages, labels=sub_domain_names, autopct='%1.1f%%', startangle=140)
plt.title("Percentage of Correct Answers by Subdomain")
plt.savefig("2.png")
plt.close()    


#combine domain and subdomains percentages    
all_category = {**domain_with_percentages,**sub_domain_with_percentages}   
print(all_category) 


#recommendation sheet
level_name = df["Level Name"].unique()
print(level_name)


recommendations_list = {}
for index, row in df.iterrows():
    # Access data from each row
    rating = row['ANXIETY-RATING SCALE']
    range = row['Range']
    level = row['Level Name']
    
    #split the range
    range = str(range)
    if "-" in range:
        lower = int(range.strip("%").split("-")[0])
        upper = int(range.strip("%").split("-")[1]) 
    elif ">" in range:
        lower = int(range.strip("%").strip(">"))
        upper = 100
    elif "<" in range:
        lower = 0
        upper = int(range.strip("%").strip("<"))
    else:
        lower = int(range.strip("%"))
        upper = lower     
  
      
    #check for recommendation
    if lower <=  all_category[level] <= upper:
        print(rating,end="\n \n")
        recommendations_list[level] = rating
        
print(recommendations_list,end="\n \n")


def create_pdf(content_dict, filename):
    # Create instance of FPDF class
    pdf = FPDF()
    
    
# Page 1: General Information
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Survey Header", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Username: {data["Username"].iloc[0]}, Age: {data["Age"].iloc[0]}", ln=True, align="L")
    pdf.ln(10)

# Page 2: Domain Percentage with Pie Chart
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Percentage of Correct Answers by Domain", ln=True, align="C")
    pdf.ln(10)
    pdf.image("1.png", x=45, y=20, w=120)


# Page 3: Subdomain Percentage with Pie Chart
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Percentage of Correct Answers by Subdomain", ln=True, align="C")
    pdf.ln(10)
    pdf.image("2.png", x=45, y=20, w=120)

    
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


create_pdf(recommendations_list, "survey_report.pdf")
