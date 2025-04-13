import numpy as np
import pandas as pd
import seaborn as sns

data = pd.read_csv("mymoviedb.csv", engine='python')
data
data.info()
data['Genre'].head()
#check Duplicate Value
data.duplicated()
data.duplicated().sum()
data.describe()
## Basics Summary Point
1. we have a data point consistent Row 9837 and column 9
2. Our data look a bit tidy not have any non and duplicate value in our data
3. Relese column date which only have yaer
4. overview and language is not a useful then remove this column
5. there is noticable outliers in popularity column
6. vote_averes is batter in catagriese
7. genre column have coama sipret value these remove white space 
row = data.iloc[1106]
print(row)
#data = data.drop(index=1106)

data.info()
data['Release_Date']=pd.to_datetime(data['Release_Date'],errors='coerce')
print(data['Release_Date'].dtypes)
data['Release_Date']=data['Release_Date'].dt.year
data['Release_Date'] = data['Release_Date'].astype('Int64') 
data.head()
## DROPING THE COLUMN
cols=['Overview','Original_Language','Poster_Url']
data.drop(cols,axis =1,inplace=True)
data.head()
def catagarize(data,col,labels):
    edges=[data[col].describe['min'],
           data[col].describe['25%'],
           data[col].describe['50%'],
           data[col].discribe['75%'],
           data[col].discribe['max']]
    data[col]=pd.cut(data[col],edges,labels=labels,duplicates='drope')
    return data
    
data['Vote_Average'].value_counts()
data['Vote_Average'].value_counts()
## Data Visualization 
sns.set_style('whitegrid')
# What is the most frequent genre of Movies  Relesed In Netflix
data['Genre'].describe()
import matplotlib.pyplot as plt
data['Genre']=data['Genre'].str.split(',')
most_common_genre = genre_df.iloc[0]
print(f"1) Most frequent genre: {most_common_genre['Genre']} ({most_common_genre['Count']} movies)")

plt.figure(figsize=(10, 6))
sns.barplot(x='Count', y='Genre', data=genre_df.head(10), palette="Blues_d")
plt.title("Top 10 Most Frequent Genres")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.tight_layout()
plt.show()
## High popularity  movies 
data.head(2)
data[data['Popularity']==data['Popularity'].max()]
## Lowe Popularity gane movies
data[data['Popularity']==data['Popularity'].min()]
## Which year whose large amount movies relised
data['Release_Date'].hist()
plt.title("Release date high")
plt.show()
### <mid>Result of this Project </mid>
