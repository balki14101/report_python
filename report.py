# import pandas as pd
# import matplotlib.pyplot as plt
# # from fpdf import FPDF
# # Read the data from the Excel file
# data = pd.read_excel("data1.xlsx")

# # Calculate the number of correct answers for each domain and subdomain
# correct_answers = data.groupby(["Domain", "Sub Domain"])["Score"].sum()

# # Calculate the total number of questions for each domain and subdomain
# total_questions = data.groupby(["Domain", "Sub Domain"])["Score"].count()
# # Calculate the percentage of correct answers for each subdomain
# subdomain_percentage = (correct_answers / total_questions) * 100


# # Group the data by "Domain" and sum the scores
# total_domain_scores = data.groupby("Domain")["Score"].sum()

# # Calculate the total number of questions attempted for each domain
# total_domain_questions = data.groupby("Domain")["Score"].count()

# # Calculate the percentage of correct answers for each domain
# domain_percentage = (total_domain_scores / total_domain_questions) * 100



# # Calculate percentages
# domain_percentages = (
#     data.groupby("Domain")["Score"].mean() * 100
# ).round(2)
# subdomain_percentages = (
#     data.groupby("Sub Domain")["Score"].mean() * 100
# ).round(2)

# print(domain_percentages)
# print(subdomain_percentages)

# # Generate pie charts
# plt.figure(figsize=(10, 6))
# plt.pie(domain_percentages["Score"], labels=domain_percentages["Domain"], autopct="%1.1f%%")
# plt.title("Percentage of Correct Answers by Domain")
# plt.savefig("domain_pie_chart.png")
# plt.close()

# plt.figure(figsize=(10, 6))
# plt.pie(subdomain_percentages["Score"], labels=subdomain_percentages["Sub Domain"], autopct="%1.1f%%")
# plt.title("Percentage of Correct Answers by Subdomain")
# plt.savefig("subdomain_pie_chart.png")
# plt.close()

# # print(correct_answers)
# # print(total_questions)
# # print(subdomain_percentage)

# # print(total_domain_scores)
# # print(total_domain_questions)
# # print(domain_percentage)


import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# Read the Excel table
data = pd.read_excel("data1.xlsx")

# Calculate percentages
domain_percentages = (
    data.groupby("Domain")["Score"].mean() * 100
).round(2).reset_index()

# getting the single domain value
filtered_data = data[data["Domain"] == "Anxiety"]
anxiety_percentage = (filtered_data["Score"].mean() * 100).round(2)
print(anxiety_percentage)

subdomain_percentages = (
    data.groupby("Sub Domain")["Score"].mean() * 100
).round(2).reset_index()

# getting the single domain value
muscular_tension_subdomain_data = data[data["Sub Domain"] == "Muscular Tension"]
situational_anxiety_subdomain_data = data[data["Sub Domain"] == "Situational Anxiety"]

muscular_tension_percentage = (muscular_tension_subdomain_data["Score"].mean() * 100).round(2)
situational_anxiety_percentage = (situational_anxiety_subdomain_data["Score"].mean() * 100).round(2)

print(muscular_tension_percentage)
print(situational_anxiety_percentage)



print(domain_percentages)
print(subdomain_percentages)
# Generate pie charts
plt.figure(figsize=(10, 6))
plt.pie(domain_percentages["Score"], labels=domain_percentages["Domain"], autopct="%1.1f%%")
plt.title("Percentage of Correct Answers by Domain")
plt.savefig("domain_pie_chart.png")
plt.close()

plt.figure(figsize=(10, 6))
plt.pie(subdomain_percentages["Score"], labels=subdomain_percentages["Sub Domain"], autopct="%1.1f%%")
plt.title("Percentage of Correct Answers by Subdomain")
plt.savefig("subdomain_pie_chart.png")
plt.close()


def get_recommendations(percentage, sheet_name="Recommendations"):

    # Read the recommendations from the Excel sheet
    df = pd.read_excel("data1.xlsx",sheet_name=sheet_name)
            
            # domain_df = df[df["Domain"] == domain]
    # df["Range"] = pd.to_numeric(df["Range"])
       # Split the "Range" column into lower and upper bounds
    df[["Lower", "Upper"]] = df["Range"].str.split("-", expand=True)
    df[["Lower", "Upper"]] = df[["Lower", "Upper"]].astype(int)

    # Find the appropriate recommendation based on the anxiety percentage
    for index, row in df.iterrows():
        # if percentage < row["Range"]:
        # if row["Lower Range"] <= percentage <= row["Upper Range"]:
        if row["Lower"] <= percentage <= row["Upper"]:
            return row["Scale"]

    # If no matching recommendation is found, return a default value
    return "No recommendation found"

# Example usage

df = pd.read_excel("data1.xlsx", sheet_name="Recommendations")

    # Find unique domain names
domains = df["Domain"].unique()
print(domains)

percentages_for_domains = {
    "Anxiety": anxiety_percentage, 
    "Muscle tension": muscular_tension_percentage,
    "Situational Anxiety": situational_anxiety_percentage
}

recommendation = get_recommendations(muscular_tension_percentage)
print(f"The recommended anxiety level for {anxiety_percentage}% anxiety is: {recommendation}")

#############################################################################################################
# Create PDF report
pdf = FPDF()


# Page 1: General Information
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Survey Header", ln=True, align="C")
pdf.ln(10)
pdf.cell(200, 10, txt=f"Username: {data["Username"].iloc[0]}, Age: {data["Age"].iloc[0]}", ln=True, align="L")
pdf.ln(10)


# pdf.add_page()

# Page 2: Domain Percentage with Pie Chart
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Percentage of Correct Answers by Domain", ln=True, align="C")
pdf.ln(10)
pdf.image("domain_pie_chart.png", x=45, y=20, w=120)
pdf.ln(85)
for index, row in domain_percentages.iterrows():
    pdf.cell(100, 10, txt=f"{row['Domain']}: {row['Score']}%", ln=True, align="L")
    pdf.ln(5)


# Page 3: Subdomain Percentage with Pie Chart
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Percentage of Correct Answers by Subdomain", ln=True, align="C")
pdf.ln(10)
pdf.image("subdomain_pie_chart.png", x=45, y=20, w=120)
pdf.ln(85)
pdf.set_font("Arial", size=12)
pdf.cell(60, 8, "Sub Domain", align="L")
pdf.cell(60, 8, "Percentage", align="L")
pdf.ln(8)
for index, row in subdomain_percentages.iterrows():
    pdf.cell(100, 10, txt=f"{row['Sub Domain']}: {row['Score']}%", ln=True, align="L")
    pdf.ln(5)


# Save the PDF report
pdf.output("report.pdf")

print("PDF report generated successfully!")
