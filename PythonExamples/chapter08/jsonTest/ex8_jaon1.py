import json

data = {
    'd':0,
    'f':9.6,
    'c':'hello world',
    'a':{
        'sbs':5
    }
}


json_data = json.dumps(data)
print(json_data)
print(type(json_data))

print()

json_data2 = json.loads(json_data)
print(json_data2)
print(type(json_data2))

print()

json_data = json.dumps(data, sort_keys=False)
print(json_data)
print(type(json_data))
