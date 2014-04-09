# Created by Chaowei Gao
# 2014.4.8
# Used to convert the play by play file from csv to json, which is comfort for D3.js

import csv
import json

def csv_to_json(filename):
    reader = csv.reader(open(filename))
    out = []
    for aline in reader:
        out.append({
            "period": aline[0],
            "time": aline[1],
            "score": aline[2],
            "team": aline[3],
            "play": aline[4:],
        })
    jsonname = filename.replace("csv", "json")
    json.dump(out, open(jsonname, "w"), indent = 4)
