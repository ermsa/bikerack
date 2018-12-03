import ast
import csv
from flask import current_app
from utils import distance


class Store:
    def __init__(self, datafile):
        with open(datafile, 'r', encoding = 'ISO-8859-1') as csvfile:
            reader = csv.DictReader(csvfile)
            self.racks = {data['INV_ID'] : data for data in reader}

    def getRacks(self):
        return self.racks

    def addRack(self, rack):
        try:
            rack = ast.literal_eval(rack)
            if rack['INV_ID'] not in self.racks:
                self.racks[rack['INV_ID']] = rack
                return f'Rack succesfully added'
            return f'This rack already exists'
        except Exception as e:
            current_app.logger.exception(e)
            return f'Rack data is invalid'

    def getRack(self, rackId):
        return self.racks.get(rackId, {})

    def removeRack(self, rackId):
        try:
            self.racks.pop(rackId)
            return f'Rack {rackId} succesfully removed'
        except KeyError:
            return f'Rack {rackId} is unknown'

    def getRacksCloseBy(self, latitude, longitude, radius):
        origin  = (float(latitude), float(longitude))
        racks = [ rack for rackId, rack in self.racks.items() if distance(origin, (float(rack['LAT']), float(rack['LONG']))) < radius ]
        return racks
