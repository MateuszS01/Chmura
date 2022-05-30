from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Quotes(Resource):
    def get(self):
        return {
        'Piosenka 1': {
        'quote': ['Tytuł: Genocide, Wykonawca: The Offspring, Format pliku: .Mp3']
    },
    'Piosenka 2': {
    'quote': ['Tytuł: Bohemian Rhapsody, Wykonawca: Queen, Format pliku: .Mp3']
    },
    'Piosenka 3': {
        'quote': ['Tytuł: Highway to Hell, Wykonawca: AC/DC, Format pliku: .Mp3']
    }
        }


api.add_resource(Quotes, '/')
if __name__ == '__main__':
    app.run(debug=True)
