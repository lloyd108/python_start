import json


data = {
    "name": "xiaohong",
    "age": 18,
    "addr": "paradise",
    "tel": 15888888888
}

with open("myJson.json", 'w', encoding='utf-8') as f:
    json.dump(data, f)


with open("myJson.json", 'r') as f:
    rst = json.load(f)

print(rst)