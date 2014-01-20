import sys

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
  
if __name__ == '__main__':
    main()