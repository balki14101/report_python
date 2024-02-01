import pandas as pd

sheet_name="Recommendations"
 # Read the Excel data
#questions sheet
data = pd.read_excel("data1.xlsx")
#recommendation sheet
df = pd.read_excel("data1.xlsx",sheet_name=sheet_name)

# Find unique domain names
domain_names = data["Domain"].unique()
# print(domain_names)

# Find unique subdomain names
sub_domain_names = data["Sub Domain"].unique()
# print(sub_domain_names)

domain_percentages = {}
for domain_name in domain_names:
    filtered_data = data[data["Domain"] == domain_name]
    correct_answers = filtered_data["Score"].sum()
    total_questions = len(filtered_data)
    percentage = (correct_answers / total_questions) * 100
    domain_percentages[domain_name] = percentage

# print(domain_percentages)

sub_domain_percentages = {}

for subdomain_name in sub_domain_names:
    filtered_data = data[data["Sub Domain"] == subdomain_name]
    correct_answers = filtered_data["Score"].sum()
    total_questions = len(filtered_data)
    percentage = (correct_answers / total_questions) * 100
    sub_domain_percentages[subdomain_name] = percentage

# print(sub_domain_percentages)
    
#combine domain and subdomains percentages    
all_category = {**domain_percentages,**sub_domain_percentages}   
print(all_category) 


#recommendation sheet
level_name = df["Level Name"].unique()
print(level_name)


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








# getting the single domain value
# filtered_data = df[df["Domain"] == "Anxiety"]
# anxiety_percentage = (filtered_data["Score"].mean() * 100).round(2)
# print(anxiety_percentage)

# getting the single domain value
# muscular_tension_subdomain_data = df[df["Sub Domain"] == "Muscular Tension"]
# situational_anxiety_subdomain_data = df[df["Sub Domain"] == "Situational Anxiety"]

# muscular_tension_percentage = (muscular_tension_subdomain_data["Score"].mean() * 100).round(2)
# situational_anxiety_percentage = (situational_anxiety_subdomain_data["Score"].mean() * 100).round(2)

percentages = [55, 68, 32]

def print_scale_and_domain(percentage, domain_name ):
   

    df[["Lower", "Upper"]] = df["Range"].str.split("-", expand=True)
    df[["Lower", "Upper"]] = df[["Lower", "Upper"]].astype(int)

    # Filter for the specific domain
    filtered_df = df[df["Domain"] == domain_name]

    # Find the matching scale
    scale_row = filtered_df.loc[(filtered_df["Lower"] <= percentage) & (percentage <= filtered_df["Upper"])]

    if not scale_row.empty:  # Scale found
        scale = scale_row["Scale"].values[0]
        print(f"Scale for {domain_name} with {percentage}%: {scale}")
    else:
        print(f"No scale found for {domain_name} with {percentage}%.")

# Example usage (replace with actual values and file path)
percentage = 65
domain_name = "Muscular Tension"
# for domain_name, percentage in domain_percentages.items():
    # print_scale_and_domain(percentage, domain_name)
 
