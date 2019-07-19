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
        if (api_key == ""):
            api_key = str(input("Please input your API Key here.")) 
        self.api_key = api_key
    
    def search(self, **kwargs):
        """
        Perform a search with parameters specified within 

        The API automatically returns a JSON of the search results; 
        automatically convert to a dictionary for python utility.
        """
        search_parameters = convert_kwargs(kwargs)
        search_url = 'https://api.nytimes.com/svc/search/v2/articlesearchq%s&api-key=%s' % (
                      search_parameters, self.api_key
        )
        result = requests.get(search_url)
        return result.json()
    
    def convert_kwargs(self, args):
        """
        Convert keyword arguments to strings friendly with nytimes requests.
        """
        arguments = process_input(args)
        valuestring = ''

        for keyword, value in arguments.items():
            if isinstance(value, list):
                value = ",".join(value)
                valuestring += '%s=%s' % (keyword, value)              
        return  valuestring
    
    def process_input(self, kwargs):
        """
        Ensures that all keyword arguments are UTF-8 encoded lowercase strings.

        kwargs : Input argument dictionary
        returns : Dictionary of processed arguments.
        """
        for keyword, value in kwargs.items():
            if isinstance(value, bool):
                kwargs[keyword] = str(value).lower()
            if isinstance(value, str):
                kwargs[keyword] = value.encode('utf8').lower()
            if isinstance(value, list):
                for list_key, list_val in enumerate(value):
                    kwargs[list_key] = list_val.encode('utf8').lower()
            if isisntance(value, dict):
                kwargs[keyword] = self.process_input(value)            
