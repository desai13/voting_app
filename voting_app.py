import streamlit as st
import pandas as pd
from faunadb import query as q
from faunadb.client import FaunaClient
from PIL import Image

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

image = Image.open('wales.JPG')
st.image(image, caption='Photo from the last trip to Wales')

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
    st.write(f'{max(borda_score, key=borda_score.get)} wins election!')
    st.bar_chart(borda_barchart)

expander = st.expander("FAQ")
expander.write("How are votes counted? Using the Borda Count - https://en.wikipedia.org/wiki/Borda_count#Borda's_original_counting")