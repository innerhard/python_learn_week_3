import csv
with open('clients.csv', 'w', encoding='utf-8') as myfile:
    mass_clients = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]
    fields = ['name', 'age', 'job']
    writing = csv.DictWriter(myfile,fields, delimiter=";")
    writing.writeheader()
    for client in mass_clients:
        writing.writerow(client)