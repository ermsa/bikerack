from flask import jsonify, current_app
from flask_restful import Resource

class root(Resource):
    def get(self, name):
        return f'welcome to my api, {name}', 200

class racks(Resource):
    def get(self):
        return jsonify(current_app.store.getRacks())

class rack(Resource):
    def get(self, rackId):
        return jsonify(current_app.store.getRack(rackId))

    def delete(self, rackId):
        return current_app.store.removeRack(rackId), 204

class racksCloseBy(Resource):
    def get(self, latitude, longitude):
        return jsonify(current_app.store.getRacksCloseBy(latitude, longitude, 0.5))

