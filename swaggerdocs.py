racksData = {
    '1551304':
    {
                "AIRE": "", 
                "ANCRAGE": "", 
                "ANC_NUM": "6133", 
                "BASE": "NON", 
                "CATEGORIE": "Support v\u00e9lo", 
                "CATL_MODELE": "24,03", 
                "CE_NO": "61", 
                "CONDITION": "", 
                "COULEUR": "", 
                "DATE_INSPECTION": "", 
                "ELEMENT": "Support v\u00e9lo SUV", 
                "EMPL_ID": "1542968", 
                "EMPL_X": "271912.038", 
                "EMPL_Y": "5035868.725", 
                "EMPL_Z": "0", 
                "INTERVENTION": "", 
                "INV_CATL_NO": "688", 
                "INV_ID": "1551304", 
                "INV_NO": "INV-1551304", 
                "LAT": "45.461973", 
                "LONG": "-73.920547", 
                "MARQ": "Support \u00e0 bicyclettes \u00e0 haute densit\u00e9 7 places (cp-7)", 
                "MATERIAU": "", 
                "ORDRE_AFFICHAGE": "2", 
                "PARC": "CAP-SAINT-JACQUES", 
                "STATUT": "Actif", 
                "TERRITOIRE": "6;"
    }, 
    "1551305": 
    {
                "AIRE": "", 
                "ANCRAGE": "", 
                "ANC_NUM": "6190", 
                "BASE": "NON", 
                "CATEGORIE": "Support v\u00e9lo", 
                "CATL_MODELE": "24,03", 
                "CE_NO": "61", 
                "CONDITION": "", 
                "COULEUR": "", 
                "DATE_INSPECTION": "", 
                "ELEMENT": "Support v\u00e9lo SUV", 
                "EMPL_ID": "1542969", 
                "EMPL_X": "271678.259", 
                "EMPL_Y": "5036674.927", 
                "EMPL_Z": "0", 
                "INTERVENTION": "", 
                "INV_CATL_NO": "688", 
                "INV_ID": "1551305", 
                "INV_NO": "INV-1551305", 
                "LAT": "45.469216", 
                "LONG": "-73.923591", 
                "MARQ": "Support \u00e0 bicyclettes \u00e0 haute densit\u00e9 7 places (cp-7)", 
                "MATERIAU": "", 
                "ORDRE_AFFICHAGE": "2", 
                "PARC": "CAP-SAINT-JACQUES", 
                "STATUT": "Actif", 
                "TERRITOIRE": "6;"
    } 
}


docRootGet = {
        'tags': ['root'],
        'description': 'Greats user',
        'parameters': [{'name': 'name',
                        'in': 'path',
                        'type': 'string'
                       }],
        'responses': {
            '200': {
                'description': 'name',
                'examples': {
                    'application/json': 'welcome to the bikerack api, JF'
                }
            }
        }
}

docRacksGet =  {
        'tags': ['rack'],
        'description': 'Get all racks data',
        'parameters': [],
        'responses': {
            '200': {
                'description': 'Racks data',
                'examples': racksData

                }
            }
        }

def docRacksPost(parser):
    return {
        'tags': ['racks'],
        'description': 'Adds a single rack',
        'reqparser': {'name': 'rack parser',
                      'parser': parser},
        'responses': {
            '201': {
                'description': 'Created rack',
                'examples': {
                    'application/json': "Rack succesfully added"

                }
            }
        }
    }


docRackGet = { 'tags': ['racks'],
        'description': 'Get all racks data',
        'parameters': [{'name': 'rackId',
                         'in': 'path',
                         'type': 'string'
                       }],
        'responses': {
            '200': {
                'description': 'Rack data',
                'examples': racksData['1551304']
                }
            }
        }

docRackDel = {
        'tags': ['rack'],
        'description': 'Delete rack by ID',
        'parameters': [{'name': 'rackId',
                        'in': 'path',
                        'type': 'string'
                       }],
        'responses': {
            '204': {
                'description': 'name',
                'examples': {
                    'application/json': 'Rack 1551304 succesfully removed'
                    }
                }
            }
        }

docRacksCloseByGet =  {
        'tags': ['racks'],
        'description': 'Get all racks data close to location',
        'parameters': [{'name': 'latitude',
                        'in': 'path',
                        'type': 'string'
                       },
                       {'name': 'longitude',
                        'in': 'path',
                        'type': 'string'
                       }],
        'responses': {
            '200': {
                'description': 'Racks data close by',
                'examples': racksData
                }
            }
        }
