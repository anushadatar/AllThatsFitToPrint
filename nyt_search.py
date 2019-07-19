#!/usr/bin/env python3
"""
Wrapper for the New York Times search API
"""
import requests

"""
To use this library, fill in your application-specific api key from the 
New York Times developer console and fill it in here.
"""
API_KEY = ""


class search_api:
"""
Search API object that can be instantiated for quick use of the NYTimes search
API in python
"""
    def __init__(self, api_key):
        """
        Initializes an instance of the search api using a development key.
        api_key = String api key associated with developer account.
        """
        if (api_key = ""):
            api_key = str(input("Please input your API Key here.") 
        self.api_key = api_key
    
    def search(self, **kwargs):
        """
        Perform a search with parameters specified within 

        The API automatically returns a JSON of the search results; 
        automatically convert to a dictionary for python utility.
        """
        search_parameters = convert_kwargs(**kwargs)
        search_url = 'https://api.nytimes.com/svc/search/v2/articlesearch.' /
                     'q%s&api-key=%s' % 
                      (search_parameters, self.api_key)
        result = requests.get(search_url)
        return result.json()
    
    def convert_kwargs(**kwargs):
        """
        Convert keyword arguments to strings friendly with nytimes requests.
        """

