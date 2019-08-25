#!/usr/bin/env python

from nyt_search import *

api = search_api('yP1rpdAAxAK6j8qXAkWN32l8jNtD195f')
i = 0
while i < 100:
    articles = api.search(i, q = 'Ross+Douthat')
    titles = api.extract_oped_titles(articles)
    i += 1
