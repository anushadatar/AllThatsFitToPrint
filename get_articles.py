#!/usr/bin/env python

from nyt_search import *

api = search_api('yP1rpdAAxAK6j8qXAkWN32l8jNtD195f')
articles = api.search(q = 'Ross+Douthat')
titles = api.extract_oped_titles(articles)
print(titles)
