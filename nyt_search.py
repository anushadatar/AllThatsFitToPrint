#!/usr/bin/env python3
"""
Wrapper for the New York Times search API
"""

import json
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
    
    def convert_kwargs(self, args):
        """
        Convert keyword arguments to strings friendly with nytimes requests.
        """
        arguments = self.process_input(args)
        valuestring = ''

        for keyword, value in arguments.items():
               valuestring += "%s=%s" % (keyword, value)

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
            if isinstance(value, dict):
                kwargs[keyword] = self.process_input(value)            
        return kwargs

    def search(self, page=1, **kwargs):
        """
        Perform a search with parameters specified within the keyword args. 

        The API automatically returns a JSON of the search results; 
        automatically convert to a dictionary for python utility.
        """
        search_parameters = self.convert_kwargs(kwargs)
        search_url = 'http://api.nytimes.com/svc/search/v2/articlesearch.json?%s&page=%i&api-key=%s' % (
                      search_parameters, page, self.api_key
        )
        result = requests.get(search_url)
        return result.json()

    def extract_oped_titles(self, json_file):
        title_array = []
        for article in json_file['response']['docs']:
            if article[u'type_of_material'] == 'Op-Ed':
                title = article['headline']['main']
                print(title)
                title_array.append(title.encode('ascii', 'ignore'))
