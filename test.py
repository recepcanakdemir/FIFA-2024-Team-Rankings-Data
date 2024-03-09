import re
import json

test = "Fenerbah\u00e7e"
uw = '\u00e7'
if  uw in test:
    deneme = test.replace(uw,'ç')
data = []
data.append(deneme)

file_path = "C:/Users/Recep Can/Desktop/FIFA Kura Çekme/Data/pr.json"
# Write JSON data to the file
with open(file_path, 'w') as json_file:
    json.dump(deneme, json_file, indent=4)
print("Data saved to:", file_path)