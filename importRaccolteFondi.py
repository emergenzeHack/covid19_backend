import csv
from server import process_report
with open('1.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(list(row))
        line_count+=1
        if line_count > 0:
            print(line_count)
            row2 = {k: v for k, v in row.items() if v is not None and v is not ""}
            print(row2)
            process_report(row2, "Raccolte fondi")
