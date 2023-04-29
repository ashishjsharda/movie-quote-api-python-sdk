import requests_mock
from quote_api import QuoteAPI
from movie_api import MovieAPI

# Update this to match the URL of your local Mockoon server
base_url = "http://localhost:3001"

# Create instances of the MovieAPI and QuoteAPI classes
movie_api = MovieAPI(base_url)
quote_api = QuoteAPI(base_url)

def test_get_movies():
    with requests_mock.Mocker() as mock:
        # Set up a mock response for the /movie endpoint
        mock.get(f"{base_url}/movie", json=[{"id": 1, "title": "The Godfather", "year": 1972}])

        # Call the get_movies method and assert that it returns the expected data
        movies = movie_api.get_movies()
        assert movies == [{"id": 1, "title": "The Godfather", "year": 1972}]

def test_get_quotes():
    with requests_mock.Mocker() as mock:
        # Set up a mock response for the /quote endpoint
        mock.get(f"{base_url}/quote", json=[{"id": 1, "text": "I'll be back", "movie_id": 123}])

        # Call the get_quotes method and assert that it returns the expected data
        quotes = quote_api.get_quotes()
        assert quotes == [{"id": 1, "text": "I'll be back", "movie_id": 123}]

def test_create_movie():
    with requests_mock.Mocker() as mock:
        # Set up a mock response for the POST /movie endpoint
        mock.post(f"{base_url}/movie", json={"id": 2, "title": "The Godfather: Part II", "year": 1974})

        # Call the create_movie method and assert that it returns the expected data
        new_movie_data = {"title": "The Godfather: Part II", "year": 1974}
        new_movie = movie_api.create_movie(new_movie_data)
        assert new_movie == {"id": 2, "title": "The Godfather: Part II", "year": 1974}

def test_update_quote():
    with requests_mock.Mocker() as mock:
        # Set up a mock response for the PUT /quote/{id} endpoint
        mock.put(f"{base_url}/quote/1", json={"id": 1, "text": "I'll be back!", "movie_id": 123})

        # Call the update_quote method and assert that it returns the expected data
        updated_quote_data = {"text": "I'll be back!", "movie_id": 123}
        updated_quote = quote_api.update_quote(1, updated_quote_data)
        assert updated_quote == {"id": 1, "text": "I'll be back!", "movie_id": 123}
