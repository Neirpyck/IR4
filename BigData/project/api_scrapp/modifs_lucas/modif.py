import json
with open("./test.json", "r") as f:
    data = json.load(f)

for i in range(len(data)):
    data[i]['name'] = data[i]['name'].lower()

with open("test2.json", "w") as f:
    json.dump(data, f, ensure_ascii=False)