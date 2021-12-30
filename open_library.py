import requests
# from loc import *
import numpy as np
import urllib
import json

class Open_Library_API:
    def get_book_info(self, ol_code):
        book_info = requests.get(f'https://openlibrary.org/works/{ol_code}.json').json()
        return book_info