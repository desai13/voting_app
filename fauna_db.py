from faunadb import query as q
from faunadb.client import FaunaClient

class Fauna_DB:

    def __init__(self, secret):
        self.client = FaunaClient(
            secret=secret,
            domain="db.eu.fauna.com",
            port=443,
            scheme="https"
        )

    def update(self, data):
        update = self.client.query(
            q.update(
                q.ref(q.collection("book_club"), "318318570795696320"),
                {
                    "data": data
                }
            )
        )

    def query(self):
        result = self.client.query(
            q.get(q.ref(q.collection("book_club"), "318318570795696320"))
        )
        return result

    def get_names(self):
        result = self.client.query(
            q.get(q.ref(q.collection("book_club"), "319401594655342786"))
        )
        print(result)
        return result["data"]["users"]

    def add_suggestion(self, suggestion):
        suggestions = self.get_suggestions()
        suggestions.append(suggestion)
        update = self.client.query(
            q.update(
                q.ref(q.collection("book_club"), "319402375446003910"),
                {
                    "data": {"suggestions": suggestions}
                }
            )
        )

    def get_suggestions(self):
        result = self.client.query(
            q.get(q.ref(q.collection("book_club"), "319402375446003910"))
        )
        print(result)
        return result["data"]["suggestions"]



