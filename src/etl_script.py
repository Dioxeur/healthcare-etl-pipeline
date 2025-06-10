import pandas as pd
from pymongo import MongoClient
import logging
from datetime import datetime
import os

def main():
    logging.basicConfig(
        level=logging.INFO,
        filename='/logs/etl.log', 
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='w'
    )
    logger = logging.getLogger(__name__)
    logger.info("--- TEST LOG IMMEDIATEMENT APRES BASICCONFIG ---")
    
    client = MongoClient("mongodb://admin:admin@mongo:27017/")
    db = client.healthcare_db
    collection = db.patients

    csv_files = [os.path.join("/data", f) for f in os.listdir("/data") if f.lower().endswith(".csv")]

    # Clear existing documents once before loading new files so previous
    # inserts aren't wiped out for every file processed
    logger.info(f"Deleting all documents from collection: {collection.name}")
    delete_result = collection.delete_many({})
    logger.info(f"Deleted {delete_result.deleted_count} documents.")

    for file in csv_files:
        logger.info(f"Processing {file}")
        process_csv_file(file, collection, logger)
    logger.info("ETL completed!")

def process_csv_file(filename, collection, logger):
    logger.info(f"Reading {filename}")
    df = pd.read_csv(filename, sep=';')
    
    df['Name'] = df['Name'].apply(lambda x: ' '.join(word.capitalize() for word in x.lower().split()))
    
    df['Date of Admission'] = pd.to_datetime(df['Date of Admission'], format='%d/%m/%Y')
    df['Discharge Date'] = pd.to_datetime(df['Discharge Date'], format='%d/%m/%Y')
    
    documents = df.to_dict('records')

    result = collection.insert_many(documents)
    logger.info(f"Inserted {len(result.inserted_ids)} documents from {filename}")


if __name__ == "__main__":
    start_time = datetime.now()
    logging.info(f"ETL script started at {start_time}")
    
    main()
    
    end_time = datetime.now()
    logging.info(f"ETL script finished at {end_time}, duration: {end_time - start_time}")