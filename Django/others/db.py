obj = {
    "name" : "t-shirt",
    "price" :"899",
    "size" : "L",
    "color" : "brown"
}

import json 

def readDB(filename="db.json"):
    with open(filename, mode='r') as jsonFile:
        data = json.load(jsonFile)

    return data


def writeDB(obj, filename="db.json"):
    with open(filename, mode='r') as jsonFile:
        data = json.load(jsonFile)
        temp = data['database']['men']
        temp.append(obj)


    with open(filename, mode='w') as f:
        json.dump(data,f)

writeDB(obj = obj)

data = readDB()

print(data)




