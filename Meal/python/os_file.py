import os
import sys
import json

with open('data.json', 'r') as f:
    data = json.load(f)

print(data['name'])

with open('foot.txt', 'w') as fo:
    json.dump(data, fo)

