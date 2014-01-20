import sys

from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


def main():
    print('Connecting...')
    try:
        client = MongoClient('localhost', 10400)
        db = client.test_database
        print (db.collection_names())
    except ConnectionFailure, e:
        sys.stderr.write('Could not connection to MongoDB: %s' % e)
        sys.exit(1)

    assert db.connection == client
    print ('Success')

    user_doc = {
        "username" : "janedoe",
        "firstname" : "Jane",
        "surname" : "Doe",
        "dateofbirth:" : datetime(1974, 4, 12),
        "email" : "janedoe74@example.com",
        "score" : 0
    }

    db.users.insert(user_doc, safe = True)
    print ("Successfully inserted document: %s" % user_doc)
    print (db.users.length)

if __name__ == '__main__':
    main()