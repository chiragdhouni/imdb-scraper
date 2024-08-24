import pandas as pd
import json

def load_movies(file_path):
    """Load movies from a JSON file into a Pandas DataFrame."""
    try:
        # Read the JSON data into a DataFrame
        with open(file_path, 'r') as file:
            movies_data = json.load(file)
        
        # Create a DataFrame
        df = pd.DataFrame(movies_data)
        return df
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return pd.DataFrame()  # Return an empty DataFrame
    
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' contains invalid JSON.")
        return pd.DataFrame()  # Return an empty DataFrame

def suggest_movies(df, genre):
    """Suggest top 5 movies based on genre and rating."""
    if df.empty:
        print("No movie data available.")
        return
    
    # Filter movies by genre using Pandas
    try:
        filtered_movies = df[df['genres'].apply(lambda x: genre in x)]
        
        # Sort movies by rating in descending order
        sorted_movies = filtered_movies.sort_values(by='rating', ascending=False)
        
        # Get the top 5 movies
        top_movies = sorted_movies.head(5)
        
        # Display the top movies
        if not top_movies.empty:
            print(f"\nTop {len(top_movies)} {genre} movies:")
            x =1
            for i, row in top_movies.iterrows():
                print(f"\n{x}. {row['title']} (Rating: {row['rating']})")
                x = x+1
                print(f"Description: {row['description']}")
        else:
            print(f"No movies found for the genre: {genre}")

    except KeyError as e:
        print(f"Error: Missing expected column in data - {e}")

def main():
    # Load movies from the JSON file
    movie_data_file = 'imdbScraper/result.json'
    movies_df = load_movies(movie_data_file)

    print("Welcome to the Movie Suggestion Bot!")
    genre = input("Enter a genre: ").strip().capitalize()
    suggest_movies(movies_df, genre)

if __name__ == "__main__":
    while True:
        main()
        choice = input("\nDo you want to suggest more movies? (y/n): ").strip().lower()
        if choice != 'y':
            print("Thank you for using the Movie Suggestion Bot! Goodbye!")
            break
