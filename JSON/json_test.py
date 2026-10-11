import json

with open ("C:\\Users\\User\\Desktop\\Coding\\JSON\\data.json", "r", encoding="utf-8") as _f:
    json_data=json.load(_f)

print(type(json_data))
print(json_data)