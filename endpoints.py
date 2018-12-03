from flask import jsonify, current_app
from flask_restful.reqparse import RequestParser
from flask_restful_swagger_2 import swagger, Resource
from swaggerdocs import docRootGet, docRacksGet, docRacksPost, docRackGet, docRackDel, docRacksCloseByGet

parser = RequestParser()
parser.add_argument('rack', type=str, required=True)

class root(Resource):
    @swagger.doc(docRootGet)
    def get(self, name):
        return f'welcome to the bikerack api, {name}', 200

class racks(Resource):
    @swagger.doc(docRacksGet)
    def get(self):
        return jsonify(current_app.store.getRacks())

    @swagger.doc(docRacksPost(parser))
    def post(self):
        args = parser.parse_args()
        rack = args['rack']
        return current_app.store.addRack(rack), 201

class rack(Resource):
    @swagger.doc(docRackGet)
    def get(self, rackId):
        return jsonify(current_app.store.getRack(rackId))

    @swagger.doc(docRackDel)
    def delete(self, rackId):
       return current_app.store.removeRack(rackId), 204

class racksCloseBy(Resource):
    @swagger.doc(docRacksCloseByGet)
    def get(self, latitude, longitude):
        return jsonify(current_app.store.getRacksCloseBy(latitude, longitude, 0.5))

