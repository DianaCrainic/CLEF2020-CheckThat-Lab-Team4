import csv

TWEETS_FILE = "data/data2.csv"

labels = {}
c_labels = {}

with open(TWEETS_FILE, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        label = row['label']
        if label not in labels:
            labels[label] = 1
        else:
            labels[label] += 1

        c_label = row['c_label']
        if c_label not in c_labels:
            c_labels[c_label] = 1
        else:
            c_labels[c_label] += 1

print(labels)
print(c_labels)
