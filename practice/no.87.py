import json

data = {'age': 20, 'height': 182, 'year': 2005}
a = json.dumps(data)
b = json.loads(a)

print(data)
print(a)
print(b)