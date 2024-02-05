import matplotlib.pyplot as plt

# Sample data
# categories = ['Category 1', 'Category 2', 'Category 3']
# values1 = [20, 35, 30]  # Values for the first stacked bar
# values2 = [15, 25, 20]  # Values for the second stacked bar

all_category = {'Anxiety': 100.0, 'Depression': 50.0, 'Muscular Tension': 100.0, 'Self Confidence': 50.0, 'Worrying': 100.0}

# Plotting
fig, ax = plt.subplots(figsize=(8, 6))  # Adjust the figure size as needed

categories = list(all_category.keys())
print("Keys:", categories)
samplevalues = list(all_category.values())
print("Keys:", samplevalues)

str_list = ["100"] * len(samplevalues)
print("Keys:", str_list)

# # Plot the first stacked bar
# ax.barh(categories, samplevalues, label='Stack 1')

# # Plot the second stacked bar on top of the first one
# ax.barh(categories, str_list, left=samplevalues, label='Stack 2')

# Plot the first stacked bar with primary color
ax.barh(categories, samplevalues, height=0.35, label='Stack 1', color='green')

# Plot the second stacked bar with secondary color
# remaining_percentages = [100 - val for val in samplevalues]
# ax.barh(categories, remaining_percentages, left=samplevalues, height=0.35, label='Stack 2', color='red')


# Add labels and legend
ax.set_xlabel('Values')
ax.set_title('Horizontal Stacked Bar Chart')
ax.legend()

# Show the plot
plt.show()
