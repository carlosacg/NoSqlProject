
import csv
import json

# Constants to make everything easier
CSV_PATH = './books.csv'
JSON_PATH = './books.json'

# Reads the file the same way that you did
csv_file = csv.DictReader(open(CSV_PATH, 'r'))

# Created a list and adds the rows to the list
json_list = []
for row in csv_file:
    json_list.append(row)

# Writes the json output to the file
file(JSON_PATH, 'w').write(json.dumps(json_list))


