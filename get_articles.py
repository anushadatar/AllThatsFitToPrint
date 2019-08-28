#!/usr/bin/env python3

from nyt_search import *

api = search_api('yP1rpdAAxAK6j8qXAkWN32l8jNtD195f')
api.save_all_oped_titles(q = 'Ross+Douthat')
api.generate_new_titles()
