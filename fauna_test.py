# Acquire the secret and optional endpoint from environment variables
secret = "fnAEVLi3GmAAxw-j79J_ROKByvxSNecCvYh2hOEi"
secret = "fnAEVL0VnzAAwD6pAw3hp72IefpJkUhQ0SvQN6Fg"

from faunadb import query as q
from faunadb.objects import Ref
from faunadb.client import FaunaClient

client = FaunaClient(
  secret=secret,
  domain="db.eu.fauna.com",
  # NOTE: Use the correct domain for your database's Region Group.
  port=443,
  scheme="https"
)

indexes = client.query(q.paginate(q.documents(collections=Ref(id='collections'))))

print(indexes)

result = client.query(
  q.paginate(
    q.documents(q.collection("voting_ledger")),
    size=3
  )
)
print(result)

result = client.query(
  q.get(q.ref(q.collection("voting_ledger"), "312078338355101888"))
)
print(result['data'])
