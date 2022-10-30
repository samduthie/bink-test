import csv

field_names = ['address_1', 'address_2', 'address_3', 'address_4']
with open('data.csv', newline='') as f:
    reader = csv.DictReader(f, delimiter=' ', fieldnames=field_names)
    for row in reader:
        row.pop()
        for field in field_names:
            print(row[field])

