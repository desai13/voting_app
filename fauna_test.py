# secret = "fnAEVLi3GmAAxw-j79J_ROKByvxSNecCvYh2hOEi"
# secret = "fnAEVL0VnzAAwD6pAw3hp72IefpJkUhQ0SvQN6Fg"
from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient
import streamlit as st

client = FaunaClient(
  secret=st.secrets["fauna"],
  domain="db.eu.fauna.com",
  port=443,
  scheme="https"
)

result = client.query(
  q.get(q.ref(q.collection("voting_ledger"), "312085305760940232"))
)
print(result['data'])

# result = client.query(
#   q.create(
#     q.collection("voting_ledger"),
#     {
#       "data": {
#         "name": "Mountainous Thunder",
#         "element": "air",
#         "cost": 15
#       }
#     }
#   )
# )
# print(result)

result = client.query(
  q.update(
    q.ref(q.collection("voting_ledger"), "312085305760940232"),
    {
      "data": {
        "Adi": {
          "0": "Lake District",
          "1": "Yorkshire Dales",
          "2": "Wales"
        },
        "Mostafa": {
          "0": "Lake District",
          "1": "Yorkshire Dales",
          "2": "Wales"
        },
        "Saloni": {
          "0": "Lake District",
          "1": "Yorkshire Dales",
          "2": "Wales"
        },
        "Lamis": {
          "0": "Lake District",
          "1": "Yorkshire Dales",
          "2": "Wales"
        },
      }
    }
  )
)
print(result)
