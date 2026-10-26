import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('data.csv')

# Data Cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(' ','_')


# Numeric Columns Cleaning
df['price'] = df["price"].astype(str).str.replace(",","").astype(float)
df['area'] = df["area"].astype(str).str.replace(",","").astype(int)
df['rate_per_sqft'] = df["rate_per_sqft"].astype(str).str.replace(",","").astype(int)


# Categorical Columns Cleaning
df['status'] = df['status'].str.strip().str.lower()
df['rera_approval'] = df['rera_approval'].str.strip().str.lower().map({'approved by rera': True, 'not approved by rera': False})
df['flat_type'] = df['flat_type'].str.strip().str.lower()


df = df.drop_duplicates()
# print(df)
# print(df.info())



# Question 1: Which is the costliest flat ?
costliest_flat = df.loc[df["price"].idxmax()]
print(f"The costliest flat is a {costliest_flat['bhk_count']} BHK {costliest_flat['flat_type']} located in {costliest_flat['locality']}. It is priced at {costliest_flat['price']/10000000} crores and has an area of {costliest_flat['area']} sqft with a rate of {costliest_flat['rate_per_sqft']} per sqft. The flat is currently {costliest_flat['status']} and is built by {costliest_flat['builder_name']}. RERA approval status: {'Approved' if costliest_flat['rera_approval'] else 'Not Approved'}.")

# Question 2: Which locality has the hieghest average price ?
highest_avg_price_locality = df.groupby('locality')['price'].mean().idxmax()
print(f"The locality with the highest average price is {highest_avg_price_locality}.")

#Question 3: Which locality has the highest rate per square foot ?
highest_rate_locality = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
print(f"The locality with the highest rate per square foot is {highest_rate_locality}.")

# Question 4: Do Ready-to-move properties cost more than under-construction properties ?
ready_to_move_avg_price = df[df['status'] == 'ready to move']['price'].mean()
under_construction_avg_price = df[df['status'] == 'under construction']['price'].mean()

if ready_to_move_avg_price > under_construction_avg_price:
    print(f" Ready-to-move properties cost more on average than under-construction properties.")
else:
    print(f" Under-construction properties cost more on average than ready-to-move properties.") 

# Question 5: Do RERE-approved properties command a price premium ?
rera_approved_avg_price = df[df['rera_approval'] == True]['price'].mean()
rera_not_approved_avg_price = df[df['rera_approval'] == False]['price'].mean()

if rera_approved_avg_price > rera_not_approved_avg_price:
    print(" RERA-approved properties command a price premium.")
else:
    print(" RERA-approved properties do not command a price premium.")

# Question 6: How does area impact price ?
# sns.scatterplot(data=df, x='area', y='price')
# plt.show()

# Question 7. Which BHK configuration is the most expensive based on per sqft rate?
most_expensive_bhk = df.groupby('bhk_count')['rate_per_sqft'].mean().idxmax()
print(f"The most expensive BHK configuration is {most_expensive_bhk} BHK.")

# Question 8. Which property type is the costliest ?
most_expensive_property_type = df.groupby('flat_type')['price'].mean().idxmax()
print(f"The most expensive property type is {most_expensive_property_type}.")

# Question 9. Do certain builders price higher ?
print(df.groupby("company_name")["rate_per_sqft"].mean().sort_values(ascending=False).head(5))
# print name of top 5
print("The top 5 builders who price higher are:", end=" ")
top_5_builders = df.groupby("company_name")["rate_per_sqft"].mean().sort_values(ascending=False).head(5) 
for builder in top_5_builders.index:
    print(builder, end=",")

# Question 10. Are larger homes more expensive per sqft ?
sns.scatterplot(data=df, x='area', y='rate_per_sqft')
plt.show() 
