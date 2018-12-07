#!/usr/bin/python
'''
Copyright (c) 2018, S@n4n6 join us on Discord https://discord.gg/MaDteVY
All rights reserved. Example script execution: $python3.7 S@n_cache_encrypted.py cache_encryptedB.db
'''

import sqlite3
import pandas as pd
from sys import argv

script, database = argv

tables = ['CellLocation','LteCellLocation','LteCellLocationLocal','WifiLocation']

conn = sqlite3.connect(database)
for table in tables:
    df = pd.read_sql_query(f"Select Timestamp, Latitude, Longitude from {table}", conn)
    #values.astype('<M8[h]') = takes the value of the time conversion and then drops all the stuff everything after the seconds.
    df['Timestamp'] = pd.to_datetime(df.Timestamp + 978307200, unit = 's').values.astype('<M8[s]')
    df.to_csv(f'{table}.csv')


conn.close()