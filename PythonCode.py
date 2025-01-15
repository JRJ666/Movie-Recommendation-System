# -*- coding: utf-8 -*-
"""
Created on Fri May  5 18:16:12 2023

@author: 15715
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

movies = pd.read_csv("D:\AIT\Final\ml-25m\ml-25m\movies.csv")
ratings = pd.read_csv(r"D:\AIT\Final\ml-25m\ml-25m\ratings.csv")


genres = ['Action','Adventure','Animation','Children','Comedy','Crime','Documentary','Drama','Fantasy','Film-Noir','Horror','Musical','Mystery','Romance','Sci-Fi','Thriller','War','Western']
rating_list = []

for i in range(len(genres)): 
    fil = genres[i]+'_filter'
    mov = genres[i]+'_movies'
    rat = genres[i]+'_ratings'
    rat_mean = rat+'_mean'
    fil = movies['genres'].str.contains(genres[i])
    mov = movies[fil]
    rat = mov.merge(ratings, on='movieId', how='inner')
    rat_mean = round(rat['rating'].mean(), 2)
    rating_list.append(rat_mean)
    
df = {'Genre':genres, 'Genres Mean Rating':rating_list}
genres_rating = pd.DataFrame(df)
genres_rating

plt.bar(genres, rating_list)
plt.xlabel('Genres')
plt.ylabel('Genre Ratings')
plt.title('Genre Ratings')
plt.xticks(rotation=90)
plt.show()

a=movies.groupby('Year').title.count()
print('Max No.of Movies Relesed =',a.max())
for i in a.index:
    if a[i] == a.max():
        print('Year =',i)

a.describe()

plt.hist(ratings['rating'], bins=10, edgecolor='black')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.title('Distribution of Movie Ratings')
plt.show()

genre_counts = movies.iloc[:, 2:].sum().sort_values(ascending=False)

merged_data = pd.merge(movies, ratings, on='movieId')

movies['Year'] = movies['title'].str.extract('\((\d{4})\)', expand=False)

# Convert the release year to numeric
movies['Year'] = pd.to_numeric(movies['Year'])

# Merge the movies and ratings DataFrames based on the movieId column

# Create a scatter plot of movie ratings versus release year
plt.figure(figsize=(10, 6))
plt.scatter(merged_data['Year'], merged_data['rating'], alpha=0.5)
plt.xlabel('Release Year')
plt.ylabel('Rating')
plt.title('Movie Ratings versus Release Year')
plt.show()

movies['Year'] = pd.to_numeric(movies['Year'])

# Merge the movies and ratings DataFrames based on the movieId column
merged_data = pd.merge(movies, ratings, on='movieId')

filtered_data = merged_data[(merged_data['Year'] >= 1990) & (merged_data['Year'] <= 2020)]
# Count the number of ratings for each year
ratings_by_year = filtered_data.groupby('Year').size()

# Create a stacked bar chart of movie ratings by year
plt.figure(figsize=(10, 6))
ratings_by_year.plot(kind='bar', stacked=True)
plt.xlabel('Release Year')
plt.ylabel('Number of Ratings')
plt.title('Movie Ratings by Year')
plt.xticks(rotation=90)
plt.show()
#As per the above result we got to know that in 2002 has the highest number of movie releases with 311 Movies.
#On an Avg. there are around 90 Movies releasing per Year.