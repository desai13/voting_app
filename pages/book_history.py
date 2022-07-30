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

"""
## Past books
"""
col1, col2, col3 = st.columns(3)

with col1:
    st.image(f"https://covers.openlibrary.org/b/id/{catch22['covers'][1]}-L.jpg", use_column_width='always')
    st.image(f"https://covers.openlibrary.org/b/id/{passnorth['covers'][0]}-L.jpg", use_column_width='always')

with col2:
    st.image(f"https://covers.openlibrary.org/b/id/{passnorth['covers'][0]}-L.jpg", use_column_width='always')
    st.image(f"https://covers.openlibrary.org/b/id/{mad_bov['covers'][0]}-L.jpg", use_column_width='always')

with col3:
    st.image(f"https://covers.openlibrary.org/b/id/{mad_bov['covers'][0]}-L.jpg", use_column_width='always')
    st.image(f"https://covers.openlibrary.org/b/id/{passnorth['covers'][0]}-L.jpg", use_column_width='always')


