from fpdf import FPDF
import json
import matplotlib.pyplot as plt

personalDetails = '''{
    "PersonId": "P1",
    "Name": "Rohit",
    "Age": 20    
}
'''
response = '''
{
    "PersonId": "P1",
    "Name": "Rohit",
    "CompSurveyID": "CS001",
    "SurveyName": "Mental Health",
    "Question": [
        {
            "QuestionID": "QN001",
            "SurveyQuestionNo": "1",
            "Score": 1,
            "Layer": "L1",
            "Domain": "Anxiety",
            "Subdomain": "Worrying",
            "Section": "Section1"
        },
        {
            "QuestionID": "QN002",
            "SurveyQuestionNo": "2",
            "Score": 1,
            "Layer": "L1",
            "Domain": "Anxiety",
            "Subdomain": "Muscular Tension",
            "Section": "Section1"
        },
        {
            "QuestionID": "QN003",
            "SurveyQuestionNo": "2",
            "Score": 1,
            "Layer": "L1",
            "Domain": "Depression",
            "Subdomain": "Self Confidence",
            "Section": "Section1"
        },
        {
            "QuestionID": "QN004",
            "SurveyQuestionNo": "2",
            "Score": 0,
            "Layer": "L1",
            "Domain": "Depression",
            "Subdomain": "Self Confidence",
            "Section": "Section1"
        }
    ]
}
'''

recommendation = '''
{
    "scale": [
        {
            "LevelName": "Anxiety",
            "Range": "0%",
            "Rating": "nothing"
        },
        {
            "LevelName": "Anxiety",
            "Range": "0-25%",
            "Rating": "normal"
        },
        {
            "LevelName": "Anxiety",
            "Range": "50-75%",
            "Rating": "moderate"
        },
        {
            "LevelName": "Anxiety",
            "Range": "75-100%",
            "Rating": "severe"
        },
        {
            "LevelName": "Muscular Tension",
            "Range": ">63%",
            "Rating": "high"
        },
        {
            "LevelName": "Self Confidence",
            "Range": ">63%",
            "Rating": "high"
        }
    ]
}
'''

user_details = json.loads(personalDetails)

# Parse JSON string into Python dictionary
data = json.loads(response)


# Find unique domain names
domain_names = set()
for question in data["Question"]:
    domain_names.add(question["Domain"])

print(domain_names)    

# Find unique subdomain names
sub_domain_names = set()
for question in data["Question"]:
    sub_domain_names.add(question["Subdomain"])

print(sub_domain_names)   

# Calculate domain percentages
domain_with_percentages = {}
for domain_name in domain_names:
    filtered_data = [question for question in data["Question"] if question["Domain"] == domain_name]
    correct_answers = sum(question["Score"] for question in filtered_data)
    total_questions = len(filtered_data)
    percentage = (correct_answers / total_questions) * 100
    domain_with_percentages[domain_name] = percentage
domain_percentages = list(domain_with_percentages.values())

# Calculate subdomain percentages
sub_domain_with_percentages = {}
for subdomain_name in sub_domain_names:
    filtered_data = [question for question in data["Question"] if question["Subdomain"] == subdomain_name]
    correct_answers = sum(question["Score"] for question in filtered_data)
    total_questions = len(filtered_data)
    percentage = (correct_answers / total_questions) * 100
    sub_domain_with_percentages[subdomain_name] = percentage
    print(filtered_data,correct_answers,total_questions,percentage,sub_domain_with_percentages)
subdomain_percentages = list(sub_domain_with_percentages.values())


#Generating bar-chart
domain_categories = list(domain_with_percentages.keys())
domain_values = list(domain_with_percentages.values())
print("Keys:", domain_categories,domain_values)


fig, ax = plt.subplots(figsize=(10,5))  # Adjust the figure size as needed

ax.barh(domain_categories, domain_values, height=0.35, label='Score', color='green')


# Add labels and legend
ax.set_xlabel('Values')
ax.set_title('Domain - Analysis')
ax.legend()


# plot
# Rotate y-axis labels for better readability
plt.yticks(rotation=45, ha='right')  # Rotate labels 45 degrees clockwise and align to the right
plt.savefig("domain_barchart.png")
plt.close()


subdomain_categories = list(sub_domain_with_percentages.keys())
subdomain_values = list(sub_domain_with_percentages.values())
print("Keys:", subdomain_categories,subdomain_values)

fig, ax = plt.subplots(figsize=(10,5))  # Adjust the figure size as needed

ax.barh(subdomain_categories, subdomain_values, height=0.35, label='Stack 1', color='green')


# Add labels and legend
ax.set_xlabel('Values')
ax.set_title('SubDomain - Analysis')
ax.legend()

# plot
# Rotate y-axis labels for better readability
plt.yticks(rotation=45, ha='right')  # Rotate labels 45 degrees clockwise and align to the right
plt.savefig("subdomain_barchart.png")
plt.close()




#combine domain and subdomains percentages    
all_category = {**domain_with_percentages,**sub_domain_with_percentages}   
print(all_category) 

# Parse JSON string into Python dictionary
recommendation_data = json.loads(recommendation)



final_recommendations = {}

for i in recommendation_data["scale"]:
    # Access data from each row
    rating = i['Rating']
    range = i['Range']
    level = i['LevelName']
    
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

    print(lower,upper,end="\n \n")    
    #check for recommendation
    if lower <=  all_category[level] <= upper:
        print(rating,end="\n \n")
        final_recommendations[level] = rating
    else:
        final_recommendations[level] = "nil"


print(final_recommendations,end="\n \n")  


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

  
