from associate_tag_to_a_resource import associate_tag_to_a_resource
import csv

## Input ## 
# "qcs::cvm:ap-singapore:uin/200033543516:instance/ins-rgbnm7pq"
# inputObject = {
#     "TagKey": "testkey2",
#     "TagValue": "testvalue2",
#     "ResourceType": "cvm",
#     "Region": "ap-singapore",
#     "Uin": "200033543516",
#     "Id": "ins-rgbnm7pq"
# }


# Note, newline='' is a documented requirement for the csv module
# for reading and writing CSV files.
with open('input.csv', encoding='utf-8-sig', newline='') as rf:
    with open('output.txt', 'w') as wf: 
        csvreader = csv.reader(rf)

        header = []
        header = next(csvreader)

        for row in csvreader:
            TagKey = row[0]
            TagValue = row[1]
            ResourceType = row[2]
            Region = row[3]
            Uin = row[4]
            Id = row[5]

            dataObject = {
                "TagKey": TagKey,
                "TagValue": TagValue,
                "ResourceType": ResourceType,
                "Region": Region,
                "Uin": Uin,
                "Id": Id
            }
            
            resp = associate_tag_to_a_resource(dataObject)    
            wf.writelines(str(resp) + '\n')