import requests
import json
from decouple import config

# Replace 'YOUR_API_KEY' with your actual TMDb API key
API_KEY = config('TMDB_API_KEY')



def search_movies(query):
    base_url = 'https://api.themoviedb.org/3/search/movie'
    params = {
        'api_key': API_KEY,
        'query': query,
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        return None

def main():
    search_query = input("Enter a movie name to search: ")
    movies = search_movies(search_query)

    if movies:
        for movie in movies:
            print(f"Title: {movie['title']}")
            print(f"Release Date: {movie['release_date']}")
            print(f"Overview: {movie['overview']}")
            print("----")
    else:
        print("No results found for the given query.")

if __name__ == '__main__':
    main()
