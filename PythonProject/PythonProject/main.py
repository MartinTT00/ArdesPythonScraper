from datetime import datetime
from dotenv import load_dotenv
import logging
import os
import mongodb
from crawling.crawling import full_crawler
from print.print import print_func


def setup():
    load_dotenv()
    # datetime object containing current date and time
    now = datetime.now()
    datetime_string = now.strftime("%Y%m%d-%H%M%S")
    env = os.getenv('ENVIRONMENT')

    logging.basicConfig(filename='./logs/crawler-{}-{}.log'.format(datetime_string, env), encoding='utf-8',
                        level=logging.DEBUG)


if __name__ == '__main__':
    setup()
    seed_url = os.getenv('SEED_URL', 'https://ardes.bg/')
    connection_string = "mongodb://localhost:27017"
    # Start mongo connection
    mongo_client = mongodb.init_client(connection_string)
    # Mongo Database name
    db = mongo_client["scraping"]
    # Scrape Collection
    collection = db["sites_collection"]

    resource = input("Choose your fetch resource (mongo/web):")
    # If web, get data, delete old data, insert new data, show data
    if resource == "web":
        print("Fetching data from the internet...")
        scraped_links = full_crawler(seed_url, 1)
        print("Deleting old data...")
        delete_old_data = collection.delete_many({})
        print("Updating the database with up-to-date data...")
        insert_result = collection.insert_many(scraped_links)
        print("Database successfully updated with ObjectId:")
        print(insert_result.inserted_ids)
        print_func(list(scraped_links)[0]["urls"])
    # If mongo, get data from DB, print data
    elif resource == "mongo":
        print("Fetching data from the local database...")
        fetchedData = list(collection.find({}))[0]["urls"]
        print_func(fetchedData)
    # If wrong command, show error
    else:
        print("Wrong command! Please use next time one of the following: mongo/web")
