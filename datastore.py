from flask import current_app
import csv
from utils import distance

class Store:
    def __init__(self, datafile):
        with open(datafile, 'r', encoding = 'ISO-8859-1') as csvfile:
            reader = csv.DictReader(csvfile)
            self.racks = [row for row in reader]

    def getRacks(self):
        return self.racks

    def addRack(self, rackData):
        self.racks.append(rackData)

    def removeRack(self, rackId):
        for i, rack in enumerate(self.racks):
            if rack['INV_ID'] == str(rackId):
                self.racks.pop(i)
                return f'Rack {rackId} succesfully removed'
        return f'Rack {rackId} is unknown'

    def getRack(self, rackId):
        for rack in self.racks:
            if rack['INV_ID'] == str(rackId):
                return rack
        return f'Rack {rackId} is unknown'

    def getRacksCloseBy(self, latitude, longitude, radius):
        racks = [ rack for rack in self.racks if distance((float(latitude), float(longitude)), (float(rack['LAT']), float(rack['LONG']))) < radius ]
        return racks
