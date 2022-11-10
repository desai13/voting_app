import streamlit as st
import pandas as pd
from PIL import Image
import plotly.graph_objects as go
import open_library
import fauna_db
import pydeck as pdk

fauna = fauna_db.Fauna_DB(secret=st.secrets["fauna"])
names = fauna.get_names()
options = ['Memorial by Bryan Washington', 'Death and the Penguin by Andrey Kurkov', 'Giovanni\'s by James Baldwin']
number_of_options = len(options)


def calc_borda_score(df):
    borda_score = {k: 0 for k in options}
    for i in range(0, number_of_options):
        for rank in options:
            try:
                borda_score[rank] += df.iloc[i].value_counts()[rank] * (number_of_options - i)
            except KeyError:
                pass
    return borda_score


"""
# Vote
Enter your ranked vote below for for what book you'd like to read, then see the results:
"""
# audio_file = open('sounds/01. Donda Chant.mp3', 'rb')
# audio_bytes = audio_file.read()
# st.audio(audio_bytes, format='audio/mp3')

name = st.selectbox('Name?', names)
rank_1 = st.selectbox('Rank 1?', options)
options_2 = [option for option in options if option not in [rank_1]]
rank_2 = st.selectbox('Rank 2?', options_2)
options_3 = [option for option in options if option not in [rank_1, rank_2]]
rank_3 = st.selectbox('Rank 3?', options_3)

pressed = st.button('Submit vote')
if pressed:
    def add_to_ledger():
        voting_ledger[name] = {
            0: rank_1,
            1: rank_2,
            2: rank_3
        }
    try:
        add_to_ledger()
    except NameError:
        voting_ledger = {}
        add_to_ledger()

    fauna.update(voting_ledger)
    st.write("Woohoo! Thanks for voting")
if name == 'Adi':
    if st.checkbox('Show results'):
        result = fauna.query()
        voting_ledger = result['data']
        df = pd.DataFrame.from_dict(voting_ledger).T
        if name == 'Adi':
            """Voting Ledger"""
            df
        borda_score = calc_borda_score(df.T)
        borda_barchart = pd.DataFrame.from_dict(borda_score, orient='index', columns=['Votes'])
        winner = str(max(borda_score, key=borda_score.get))
        st.metric(label="Winner:", value=winner, delta=f"{borda_score[winner]} votes")
        colors = []
        for option in borda_barchart.index.values:
            if option == winner:
                colors.append('rgb(26, 118, 255)')
            else:
                colors.append('rgb(55, 83, 109)')
        fig = go.Figure(data=[go.Bar(
            x=borda_barchart.index.values,
            y=borda_barchart.Votes.values,
            marker_color=colors
        )])
        st.plotly_chart(fig, use_container_width=True)

expander = st.expander("FAQ")
expander.write("How are votes counted? Using the Borda Count - https://en.wikipedia.org/wiki/Borda_count#Borda's_original_counting")