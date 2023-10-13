from read_tags_of_a_resource import read_tags_of_a_resource
import csv
import json

## Input ## 
# "qcs::cvm:ap-singapore:uin/200033543516:instance/ins-rgbnm7pq"
# inputObject = {
#     "Id": "ins-rgbnm7pq"
# }


# Note, newline='' is a documented requirement for the csv module
# for reading and writing CSV files.
with open('input.csv', encoding='utf-8-sig', newline='') as rf:
    with open('output.json', 'w') as wf: 
        csvreader = csv.reader(rf)

        header = []
        header = next(csvreader)

        for row in csvreader:
            Id = row[0]

            dataObject = {
                "Id": Id
            }
            
            resp = read_tags_of_a_resource(dataObject)
            resp = resp.to_json_string()
            resp = json.loads(resp)
            json_object = json.dumps(resp, indent=4)
            wf.write(json_object)