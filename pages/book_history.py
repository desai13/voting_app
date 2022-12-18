import streamlit as st
import pandas as pd
from PIL import Image
import plotly.graph_objects as go
import open_library
import fauna_db

ol_api = open_library.Open_Library_API()

catch22 = ol_api.get_book_info('OL276798W')
passnorth = ol_api.get_book_info('OL35612082M')
mad_bov = ol_api.get_book_info('OL893723W')
glad_mum = ol_api.get_book_info('OL26663382W')
panenka = ol_api.get_book_info('OL27083967W')
arcadia = ol_api.get_book_info('OL1136420M')


"""
## Past books
"""
col1, col2, col3 = st.columns(3)

with col1:
    st.image(f"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.explicit.bing.net%2Fth%3Fid%3DOIP.Fkrefam90HeoI9g0GbcrCQHaLW%26pid%3DApi&f=1&ipt=132c79a5b381a3705be24f85baa2367635a0ef187442d60e173d0a8735e3aa51&ipo=images", use_column_width='always')
    st.image(f"https://images-na.ssl-images-amazon.com/images/I/714l-Ja-VAL.jpg", use_column_width='always')
    st.image(f"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.pinimg.com%2Foriginals%2Faa%2F73%2Ff7%2Faa73f7f8fca7f7b7f1092f05759cb566.jpg&f=1&nofb=1&ipt=583e53ead145305ac92ab682b32ed7f50a7ef7b8cb9bebebf74733e5f37dcfca&ipo=images", use_column_width='always')

with col2:
    st.image(f"https://covers.openlibrary.org/b/id/{passnorth['covers'][0]}-L.jpg", use_column_width='always')
    st.image(f"https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1600698058i/55410610.jpg", use_column_width='always')
    st.image(
        f"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.iX0E8rVMK9N6J0uxIVb7vwHaLb%26pid%3DApi&f=1&ipt=55bf672917cd0811e858fa557df2db73a0c9f07088a072a22e7f3cc92ba85da9&ipo=images",
        use_column_width='always')

with col3:
    st.image(f"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.explicit.bing.net%2Fth%3Fid%3DOIP.XugxyeYjZNb28yltVLswCQHaLQ%26pid%3DApi&f=1&ipt=2ba48595b89fd87c8e1b7bd6f25278420d45b10c7ab9d7c5242de87099fb3d4d&ipo=images", use_column_width='always')
    st.image(f"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.thenile.io%2Fr1000%2F9781580815963.jpg%3Fr%3D5ebd81607d294&f=1&nofb=1&ipt=ed03d94b0bf8dcca1108180fd6122f65276595dfa23483201e035b7812283b98&ipo=images", use_column_width='always')


