import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import glob

def Check_Dataframe():
   print("##########COMPLETE INFO#######################")
   print("Head\n", complete_df.head())
   print("\nInfo\n")
   complete_df.info()
   print("\nDescribe\n", complete_df.describe(include='all'))
   print("\nIsNull\n", complete_df[complete_df.isnull().any(axis = 1)])
   print("#################################")

observations_df = pd.read_csv("observations.csv")
species_df = pd.read_csv("species_info.csv")

complete_df = pd.merge(observations_df, species_df, on = 'scientific_name')

# First Check of how the Data looks like

pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)        # Prevent line wrapping
pd.set_option('display.max_colwidth', None) # Show full content of each column (if needed)
Check_Dataframe()
print(complete_df['conservation_status'].unique())
print(complete_df['category'].unique())
print(complete_df['park_name'].unique())

# Cleaning Columns

# Analysis
# 1. What is the distribution of conservation_status for animals?
sns.countplot(x= 'conservation_status', data = complete_df)
plt.show()
plt.clf()

# 2. Are certain types of species more likely to be endangered?
sns.countplot(x='category', hue='conservation_status', data=complete_df)
plt.show()
plt.clf()

# 3. Are the differences between species and their conservation status significant?

# 4. Which species were spotted the most at each park?
sns.countplot(x='park_name', hue='category', data=complete_df)
plt.show()
plt.clf()
