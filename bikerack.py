from flask import Flask
from flask_restful_swagger_2 import Resource, Api
from flask_cors import CORS
from endpoints import root, racks, rack, racksCloseBy
from datastore import Store

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(root, '/<name>')
api.add_resource(racks, '/racks')
api.add_resource(rack, '/rack/<rackId>')
api.add_resource(racksCloseBy, '/racksCloseBy/<latitude>/<longitude>')

if __name__ == '__main__':
        app.store = Store('supportvelosigs.csv')
        app.run(debug=True,host='0.0.0.0')

