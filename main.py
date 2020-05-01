from pymongo import MongoClient
import csv
import re
import pprint


client = MongoClient()
concerts_db = client['concerts']
concerts_collection = concerts_db['concert']


def read_data(csv_file, db):
    with open("artists.csv", encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for concert in reader:
            concert['Цена'] = int(concert['Цена'])
            concerts_collection.insert_one(concert)
        return concerts_collection


def find_cheapest(db):
    return list(concerts_collection.find().sort('Цена', direction=1))


def find_by_name(name, db):
    regex = re.compile(name, re.IGNORECASE)
    return list(concerts_collection.find({'Исполнитель': regex}).sort('Цена', direction=1))


 # created_db = read_data('artists.csv', concerts_collection)
# pprint.pprint(list(created_db.find()))


# cheapest_ticket = find_cheapest(concerts_collection)
# pprint.pprint(cheapest_ticket)


# found_artist = find_by_name("Зв", concerts_collection)
# pprint.pprint(found_artist)

