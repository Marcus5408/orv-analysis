from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
import json

app = Flask(__name__)
api = Api(app)

class Quote(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.quotes_file = open("quote-API\quotes.json", "r", encoding="utf-8")
        self.quotes = json.load(self.quotes)
        self.quotes_file.close()

    def get(self, id=0):
        if id == 0:
            return random.choice(self.quotes), 200

        for quote in self.quotes:
            if(quote["id"] == id):
                return quote, 200
        return "Quote not found", 404

api.add_resource(Quote, "/ai-quotes", "/ai-quotes/", "/ai-quotes/<int:id>")

if __name__ == '__main__':
    app.run(debug=True)