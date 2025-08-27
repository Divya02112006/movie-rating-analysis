import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

# Merge movies with ratings
data = pd.merge(ratings, movies, on="MovieID")

# Average rating per movie
avg_ratings = data.groupby("Title")["Rating"].mean().sort_values(ascending=False)

print("Top 5 Movies by Average Rating:")
print(avg_ratings.head())

# Plot most rated movies
movie_counts = data["Title"].value_counts().head(10)

plt.figure(figsize=(10,5))
sns.barplot(x=movie_counts.values, y=movie_counts.index, palette="viridis")
plt.title("Top 10 Most Rated Movies")
plt.xlabel("Number of Ratings")
plt.ylabel("Movie Title")
plt.show()
