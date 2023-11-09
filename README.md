
# Movie Database Python Script

This Python script allows you to search for movies using The Movie Database (TMDb) API. It fetches information about movies based on your search query and displays details about the matching movies.

## Prerequisites

- Python 3.x installed on your system
- A valid TMDb API key. You can obtain one by signing up at [TMDb](https://www.themoviedb.org/) and generating an API key.

## Installation

1. Clone this repository or download the `movie_database.py` file.

2. Install the required Python library, `requests`, using pip:

   ```bash
   pip install requests
   ```

3. Create a `.env` file in the same directory as the `movie_database.py` file and add your TMDb API key as follows:

   ```
   TMDB_API_KEY=your_actual_api_key
   ```

   Replace `your_actual_api_key` with your TMDb API key.

## Usage

1. Open your terminal or command prompt.

2. Navigate to the directory where the `movie_database.py` script is located.

3. Run the script using the following command:

   ```bash
   python3 movie_database.py
   ```

4. Follow the on-screen instructions to enter a movie name to search for.

5. The script will display information about the matching movies, including the title, release date, and overview.

6. To exit the script, press `Ctrl + C`.

## Example

Here's an example of how to use the script:

```bash
python3 movie_database.py
Enter a movie name to search: Inception
```

The script will fetch and display information about movies with "Inception" in their title.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [The Movie Database (TMDb)](https://www.themoviedb.org/) for providing the movie data.

Feel free to modify this README to suit your project's specific requirements and provide any additional information or instructions that users may need.