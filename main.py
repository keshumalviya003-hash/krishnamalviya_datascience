import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df =pd.read_csv("movie dataset.csv")

# check missing values
# cheking missing values using isnull() and sum() functions
print(df.isnull().sum())

#handle missing values
#manage missing values by filling genre and director with "Unknown" and filling IMDb_Rating and Runtime_Min with median values
df["Genre"] = df["Genre"].fillna("Unknown")
df["Director"] = df["Director"].fillna("Unknown")
df["IMDb_Rating"] = df["IMDb_Rating"].fillna(df["IMDb_Rating"].median())
df["Runtime_Min"] = df["Runtime_Min"].fillna(df["Runtime_Min"].median())
#print(df.isnull().sum())

# Rename column for clarity
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
#print(df.columns)

#manage duplicate rows
#print("Duplicate rows before:", df.duplicated().sum())
df = df.drop_duplicates()
#print("Duplicate rows after:", df.duplicated().sum())

# movies released before the year 2000
movies_before_2000 = df[df["release_year"] < 2000][["movie_title", "release_year", "genre", "director", "imdb_rating", "runtime_min"]]
print("Movies released before the year 2000:")
print(movies_before_2000)

 #Calculate average ratings per genre
avg_ratings_per_genre = df.groupby("genre")["imdb_rating"].mean()
#print("Average ratings per genre:")
#print(avg_ratings_per_genre)

# the top 5 highest-rated movies
top_5_highest_rated_movies = df.nlargest(5, "imdb_rating")[["movie_title", "imdb_rating"]]
#print("Top 5 highest-rated movies:")
#print(top_5_highest_rated_movies)

#Create a bar chart showing the count of movies per genre
genre_counts = df["genre"].value_counts()
plt.figure(figsize=(13, 6))
sns.barplot(x=genre_counts.index, y=genre_counts.values)
plt.title("Count of Movies per Genre")
plt.xlabel("Genre")
plt.ylabel("Count")
#plt.show()

# average rating by genre 
avg_rating_by_genre = df.groupby("genre")["imdb_rating"].mean().sort_values(ascending = False)
plt.figure(figsize=(13, 6))
sns.barplot(x=avg_rating_by_genre.index, y=avg_rating_by_genre.values)
plt.title("average rating by genre")
plt.xlabel("genre")
plt.ylabel("average rating")
# plt.show()
