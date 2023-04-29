import requests

class MovieAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_movies(self):
        """
        Retrieve a list of all movies.
        """
        response = requests.get(self.base_url + "/movie")
        response.raise_for_status()  # raise an exception for non-2xx responses
        return response.json()

    def get_movie_by_id(self, movie_id):
        """
        Retrieve a single movie by ID.
        """
        response = requests.get(self.base_url + f"/movie/{movie_id}")
        response.raise_for_status()
        return response.json()

    def get_movie_quotes(self, movie_id):
        """
        Retrieve a list of quotes for a single movie by ID.
        """
        response = requests.get(self.base_url + f"/movie/{movie_id}/quote")
        response.raise_for_status()
        return response.json()

    def create_movie(self, movie_data):
        """
        Create a new movie.
        """
        response = requests.post(self.base_url + "/movie", json=movie_data)
        response.raise_for_status()
        return response.json()

    def update_movie(self, movie_id, movie_data):
        """
        Update an existing movie by ID.
        """
        response = requests.put(self.base_url + f"/movie/{movie_id}", json=movie_data)
        response.raise_for_status()
        return response.json()

    def delete_movie(self, movie_id):
        """
        Delete a movie by ID.
        """
        response = requests.delete(self.base_url + f"/movie/{movie_id}")
        response.raise_for_status()
