
from flask import jsonify, request
import numpy as np
import pandas as pd
from collections import defaultdict
from src.models.AzmoonGradeDocument import AzmoonGradeDocument
import time

def insertAzmoon():

    agDoc = AzmoonGradeDocument()
    json = request.get_json()
    try:
        start_time = time.time()
        azmoonDoc = agDoc.Calculate(json)
        print("--- %s seconds ---" % (time.time() - start_time))

        return jsonify({"message": "azmoon grade imported successfully", "data":{"_id": str(azmoonDoc), "time":time.time() - start_time} }), 200
    except:
        return jsonify({"message": "Oops...import azmoon failed"}), 500
    


def getAzmoon(azmoonId):
    azmoonId = azmoonId
    print(azmoonId)
    agDoc = AzmoonGradeDocument()
    try:
        azmoonDoc = agDoc.schema.find_one({"_id": azmoonId})
        
        return jsonify({"message": "azmoon grade get successfully", "data":azmoonDoc}), 200
    except:
        return jsonify({"message": "Oops...import azmoon failed"}), 500