import os
import sys
import json
import certifi
import pandas as pd
import numpy as np
import pymongo
from dotenv import load_dotenv
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

# Load environment variables
load_dotenv()

# MongoDB URL from environment variable
MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

# MongoDB client certificate
ca = certifi.where()

class NetworkDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def csv_to_json_convertor(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def insert_data_mongodb(self, records, database, collection):
        try:
            self.database = database
            self.collection = collection
            self.records = records

            # Connect to MongoDB using the URL
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=ca)
            self.database = self.mongo_client[self.database]

            # Insert data into the specified collection
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

if __name__ == '__main__':
    # Define file path, database, and collection
    FILE_PATH = "Network_Data/phisingData.csv"
    DATABASE = "KOUSHIK"
    COLLECTION = "networkData"

    # Create instance of NetworkDataExtract
    networkobj = NetworkDataExtract()

    # Convert CSV to JSON records
    records = networkobj.csv_to_json_convertor(file_path=FILE_PATH)

    # Insert data into MongoDB and get the number of records inserted
    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, COLLECTION)

    # Output the results
    print(records)
    print(f"Number of records inserted: {no_of_records}")
