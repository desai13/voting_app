import streamlit as st
import pandas as pd
from faunadb import query as q
from faunadb.client import FaunaClient
from PIL import Image
import plotly.graph_objects as go
import pydeck as pdk


names = ['Adi', 'Mostafa', 'Lamis', 'Saloni', 'Mo', 'Dhanya', 'Alice', 'Alex', 'Katie', 'Gianni']
options = ['Lake District', 'Yorkshire Dales', 'Wales']
number_of_options = len(options)

client = FaunaClient(
  secret=st.secrets["fauna"],
  domain="db.eu.fauna.com",
  port=443,
  scheme="https"
)


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
# Vote for the next trip location!
Enter your ranked vote below, then see the results:
"""
audio_file = open('myaudio.ogg', 'rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes, format='audio/ogg')

image = Image.open('wales.JPG')
st.image(image, caption='Photo from the last trip to Wales')

if st.checkbox('Show locations on a map'):
    coords = [[53.128075, -3.414560], [54.014785, -1.734826], [54.473345, -3.556881]]
    maps = pd.DataFrame(coords, columns=['lat', 'lon'])
    st.map(maps)

    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/light-v9',
        initial_view_state=pdk.ViewState(
            latitude=53,
            longitude=-3,
            zoom=7,
            pitch=50,
        ),
        layers=[
           pdk.Layer(
               'HexagonLayer',
               data=maps,
               get_position='[lon, lat]',
               radius=200,
               elevation_scale=50,
               elevation_range=[0, 1000],
               pickable=True,
               extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=maps,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=3000,
            ),
        ],
    ))

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

    update = client.query(
        q.update(
            q.ref(q.collection("voting_ledger"), "312085305760940232"),
            {
                "data": voting_ledger
            }
        )
    )
    st.write("Woohoo! Thanks for voting")

if st.checkbox('Show results'):
    result = client.query(
        q.get(q.ref(q.collection("voting_ledger"), "312085305760940232"))
    )
    voting_ledger = result['data']
    df = pd.DataFrame.from_dict(voting_ledger).T
    if name == 'Adi':
        """Voting Ledger"""
        df
    borda_score = calc_borda_score(df.T)
    borda_barchart = pd.DataFrame.from_dict(borda_score, orient='index', columns=['Votes'])
    winner = str(max(borda_score, key=borda_score.get))
    st.metric(label="Winner:", value=winner, delta=f"{borda_score[winner]} votes")
    # st.bar_chart(borda_barchart)
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
    # fig.update_layout(title_text='Least Used Feature')
    st.plotly_chart(fig, use_container_width=True)

expander = st.expander("FAQ")
expander.write("How are votes counted? Using the Borda Count - https://en.wikipedia.org/wiki/Borda_count#Borda's_original_counting")