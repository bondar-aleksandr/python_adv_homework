import csv

FileError = csv.Error


def load(file):
    reader = csv.reader(file)
    data = {}
    for line in reader:
        data[line[0]] = line[1]
    return data


def dump(data: dict, file):
    writer = csv.writer(file)
    for name, phone in data.items():
        writer.writerow([name, phone])