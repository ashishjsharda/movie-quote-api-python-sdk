from movie_api import MovieAPI
import requests_mock


def test_get_movie_quotes():
    with requests_mock.Mocker() as m:
        # Mock the movie quotes endpoint
        mock_quotes = [{'id': 1, 'text': 'I\'ll be back', 'movie_id': 123}]
        m.get('http://localhost:3001/movie/123/quote', json=mock_quotes)

        # Create a new instance of the MovieAPI class and call the get_movie_quotes() function
        movie_api = MovieAPI('http://localhost:3001')
        quotes = movie_api.get_movie_quotes(123)

        # Verify that the function returned the expected quotes
        assert quotes == mock_quotes


