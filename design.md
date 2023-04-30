

# Movie Quote API Python SDK Design

## Overview

The movie-quote-api-python-sdk is a software development kit (SDK) that provides a Python interface for accessing the Movie Quote API. 

## SDK Structure

The SDK consists of two main classes: `MovieAPI` and `QuoteAPI`. These classes provide methods for interacting with the `/movie` and `/quote` endpoints of the Movie Quote API, respectively. Each class corresponds to a specific endpoint of the API, and provides methods for retrieving, creating, updating, and deleting resources.

The `MovieAPI` class has the following methods:

-   `get_movies()`: retrieves a list of all movies from the `/movie` endpoint.
-   `get_movie_by_id(movie_id)`: retrieves a specific movie by its ID from the `/movie/{id}` endpoint.
-   `get_movie_quotes(movie_id)`: retrieves all quotes for a specific movie by its ID from the `/movie/{id}/quote` endpoint.

The `QuoteAPI` class has the following methods:

-   `get_quotes()`: retrieves a list of all quotes from the `/quote` endpoint.
-   `get_quote_by_id(quote_id)`: retrieves a specific quote by its ID from the `/quote/{id}` endpoint.
-   `create_quote(quote_data)`: creates a new quote with the specified data.
-   `update_quote(quote_id, quote_data)`: updates an existing quote with the specified ID and data.
-   `delete_quote(quote_id)`: deletes an existing quote with the specified ID.

The SDK also includes an `__init__.py` file that provides a high-level interface for accessing the API. This file imports the `MovieAPI` and `QuoteAPI` classes and exposes them as top-level objects, making it easy for developers to access the API without having to import individual modules.

## API Interaction

The SDK interacts with the Movie Quote API using the `requests` library. Each method in the `MovieAPI` and `QuoteAPI` classes sends an HTTP request to the corresponding endpoint of the API and returns the response as a Python object. The SDK also includes error handling code that checks the response status code and raises an exception if an error occurs.

The SDK does not mirror the API exactly. Instead, it provides a higher-level interface that abstracts away some of the details of the API. For example, the `MovieAPI.get_movie_quotes()` method combines calls to the `/movie/{id}` and `/movie/{id}/quote` endpoints to retrieve all quotes for a specific movie.

## Design Decisions

The SDK is designed with simplicity and ease-of-use in mind. It provides a high-level interface for accessing the Movie Quote API that abstracts away some of the details of HTTP requests and responses. The SDK uses the `requests` library for sending HTTP requests and handling responses, which is a widely-used and well-documented library that is familiar to many Python developers.

One design decision that we made was to combine calls to the `/movie/{id}` and `/movie/{id}/quote` endpoints in the `MovieAPI.get_movie_quotes()` method. This decision was made to simplify the API interface and reduce the number of requests required to retrieve all quotes for a specific movie.

Another design decision that we made was to use the `requests_mock` library for testing the SDK. This library provides a simple and powerful way to mock HTTP requests and responses, making it easy to test the SDK's behavior under various conditions.





