# ============================================
# MOVIE RECOMMENDATION SYSTEM
# ============================================

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ============================================
# 1. LOAD MOVIE DATASET
# ============================================

# Read the CSV file
df = pd.read_csv("movie_dataset.csv")

# Combine genre and keywords into one column
df["features"] = df["genre"] + " " + df["keywords"]

print("\nDataset loaded successfully!")
print("\nMovie Dataset:")
print(df[["title", "genre", "keywords"]])


# ============================================
# 2. CONVERT TEXT INTO TF-IDF VECTORS
# ============================================

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Convert movie features into numerical vectors
tfidf_matrix = vectorizer.fit_transform(df["features"])

print("\nTF-IDF Matrix Shape:")
print(tfidf_matrix.shape)


# ============================================
# 3. CALCULATE COSINE SIMILARITY
# ============================================

# Calculate similarity between all movies
similarity_matrix = cosine_similarity(tfidf_matrix)


# ============================================
# 4. MOVIE RECOMMENDATION FUNCTION
# ============================================

def recommend_movies(movie_name, number=5):

    # Remove unnecessary spaces and convert to lowercase
    movie_name = movie_name.strip().lower()

    # Find the movie in the dataset
    matching_movies = df[
        df["title"].str.lower() == movie_name
    ]

    # Check if movie exists
    if matching_movies.empty:

        print("\nMovie not found!")
        print("Please enter a movie from the available list.")

        return

    # Get index of selected movie
    movie_index = matching_movies.index[0]

    # Get similarity scores for selected movie
    similarity_scores = similarity_matrix[movie_index]

    # Sort movies according to similarity
    similar_movies = np.argsort(similarity_scores)[::-1]

    # Store recommendations
    recommendations = []

    for index in similar_movies:

        # Do not recommend the movie itself
        if index == movie_index:
            continue

        recommendations.append({
            "title": df.iloc[index]["title"],
            "score": similarity_scores[index]
        })

        # Stop after required number of recommendations
        if len(recommendations) == number:
            break

    # Convert recommendations into DataFrame
    recommendations_df = pd.DataFrame(recommendations)


    # ========================================
    # 5. DISPLAY RECOMMENDATIONS
    # ========================================

    print("\n============================================")
    print("          RECOMMENDED MOVIES")
    print("============================================")

    print("\nYou selected:", df.iloc[movie_index]["title"])

    print("\nBased on your selection, you may also like:\n")

    for i, row in recommendations_df.iterrows():

        print(
            f"{i + 1}. {row['title']} "
            f"(Similarity Score: {row['score']:.2f})"
        )


    # ========================================
    # 6. CREATE GRAPH USING MATPLOTLIB
    # ========================================

    plt.figure(figsize=(10, 5))

    plt.bar(
        recommendations_df["title"],
        recommendations_df["score"]
    )

    plt.title(
        "Movie Recommendation Similarity Scores"
    )

    plt.xlabel("Recommended Movies")

    plt.ylabel("Similarity Score")

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    plt.show()


# ============================================
# 7. MAIN PROGRAM
# ============================================

print("\n============================================")
print("       MOVIE RECOMMENDATION SYSTEM")
print("============================================")

print("\nAvailable Movies:\n")

for title in df["title"]:
    print("-", title)


# Ask the user for a movie
movie_name = input(
    "\nEnter the name of a movie: "
)


# Generate recommendations
recommend_movies(movie_name)


