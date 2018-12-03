# Bikerack

## Api to find a nearby bike rack in Montreal

### This project provides API endpoints to acces data of bike racks in Montreal.

### Data is provided by the city open data project: http://donnees.ville.montreal.qc.ca/dataset/arceaux-velos

### To install locally:

#### Run:
1. `git clone https://github.com/ermsa/bikerack.git`
2. `cd bikerack`
3. `docker build . -t bikerack:latest`
4. `docker pull swaggerapi/swagger-ui`
5. `docker run -p 5000:5000 bikerack`
6. `docker run -p 80:8080 -e API_URL=http://localhost:5000/api/swagger.json swaggerapi/swagger-ui`

#### Point your browser to http://localhost/ to access via swagger or access/curl to http://localhost:5000/

![landing page image](https://github.com/ermsa/bikerack/blob/master/bikerack.jpg)











