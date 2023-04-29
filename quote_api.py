import requests

class QuoteAPI:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_quotes(self):
        """
        Retrieve a list of all quotes.
        """
        response = requests.get(self.base_url + "/quote")
        response.raise_for_status()  # raise an exception for non-2xx responses
        return response.json()

    def get_quote_by_id(self, quote_id):
        """
        Retrieve a single quote by ID.
        """
        response = requests.get(self.base_url + f"/quote/{quote_id}")
        response.raise_for_status()
        return response.json()

    def create_quote(self, quote_data):
        """
        Create a new quote.
        """
        response = requests.post(self.base_url + "/quote", json=quote_data)
        response.raise_for_status()
        return response.json()

    def update_quote(self, quote_id, quote_data):
        """
        Update an existing quote by ID.
        """
        response = requests.put(self.base_url + f"/quote/{quote_id}", json=quote_data)
        response.raise_for_status()
        return response.json()

    def delete_quote(self, quote_id):
        """
        Delete a quote by ID.
        """
        response = requests.delete(self.base_url + f"/quote/{quote_id}")
        response.raise_for_status()
