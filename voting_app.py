import streamlit as st
import pandas as pd
import json

"""
# Voting app
Enter your ranked vote below, then see the results:
"""

with open('myfile.json') as json_file:
    voting_ledger = json.load(json_file)

names = ['Adi', 'Mostafa', 'Lamis', 'Saloni', 'Mo', 'Dhanya', 'Alice', 'Alex', 'Katie', 'Gianni']
options = ['Lake District', 'Yorkshire Dales', 'Wales']
number_of_options = len(options)

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

    out_file = open("myfile.json", "w")
    json.dump(voting_ledger, out_file, indent=6)
    out_file.close()

    votes = pd.read_json('myfile.json').T
    st.write("Woohoo! Thanks for voting")

# reading votes from JSON
votes = pd.read_json('myfile.json').T
df = pd.DataFrame.from_dict(voting_ledger).T
df = votes.copy()

# calculating Borda scores from votes
borda_score = {k: 0 for k in options}
for i in range(0, number_of_options):
    for rank_1 in options:
        try:
            borda_score[rank_1] += df[i].value_counts()[rank_1] * (number_of_options - i)
        except KeyError:
            pass

# displaying vote count in bar chart
borda_barchart = pd.DataFrame.from_dict(borda_score, orient='index', columns=['Votes'])

if st.checkbox('Show results'):
    if name == 'Adi':
        """Voting Ledger"""
        votes
    st.write(f'{max(borda_score, key=borda_score.get)} wins election!')
    st.bar_chart(borda_barchart)

expander = st.expander("FAQ")
expander.write("How are votes counted? Using the Borda Count - https://en.wikipedia.org/wiki/Borda_count#Borda's_original_counting")