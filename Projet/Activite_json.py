import json
import Activite as ins

with open("../BDactivite.json") as var:
    json_data = json.load(var)

    for item in json_data["data"]:
        activ = ins.Activite(item["ActCode"], item["ActLib"], item["EquipementId"])

        print (activ.display_nomAct())