Python 3.7 

Instructions:

Need to have pulled the cache_encryptedB.db from an iOS device. 

This script is able to pull the location data from the following tables CellLocation, LteCellLocation, LteCellLocationLocal, and WifiLocation. 

There are two posted scripts one S@n_cache_encryptedB.py that just contains the timestamp, latitude, and longitude which makes it easier to import into Google Earth. 

The other S@n_cache_encryptedB_all.py that pulls all columns from within the tables. 

To import this into Google Earth just launch Google Earth and goto file/import and point it to the pulled csv files. 

Example: $ $python3.7 S@n_cache_encrypted.py cache_encryptedB.db

Work in progress: 

I am working on getting the data to populate within Google Maps to view data/time stamps.

