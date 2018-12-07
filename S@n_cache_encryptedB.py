#!/usr/bin/python
'''
Copyright (c) 2018, S@n4n6 join us on Discord https://discord.gg/MaDteVY
All rights reserved.
'''

import sqlite3
import pandas as pd
import datetime, pytz
import csv

conn = sqlite3.connect("cache_encryptedB.db")
df = pd.read_sql_query("Select Timestamp, Latitude, Longitude from CellLocation", conn)

df['Timestamp'] = pd.to_datetime(df.Timestamp + 978307200, unit ='s')

df.to_csv('Cache_encryptedB.csv')

conn.close()

conn = sqlite3.connect("cache_encryptedB.db")
df = pd.read_sql_query("Select Timestamp, Latitude, Longitude from LteCellLocation", conn)

df['Timestamp'] = pd.to_datetime(df.Timestamp + 978307200, unit ='s')

df.to_csv('LteCellLocation.csv')

conn.close()

conn = sqlite3.connect("cache_encryptedB.db")
df = pd.read_sql_query("Select Timestamp, Latitude, Longitude from LteCellLocationLocal", conn)

df['Timestamp'] = pd.to_datetime(df.Timestamp + 978307200, unit ='s')

df.to_csv('LteCellLocationLocal.csv')

conn.close()

conn = sqlite3.connect("cache_encryptedB.db")
df = pd.read_sql_query("Select Timestamp, Latitude, Longitude from WifiLocation", conn)

df['Timestamp'] = pd.to_datetime(df.Timestamp + 978307200, unit ='s')

df.to_csv('WifiLocation.csv')

conn.close()

conn = sqlite3.connect("cache_encryptedB.db")
df = pd.read_sql_query("Select Timestamp, Latitude, Longitude from LteCellLocation", conn)

df['Timestamp'] = pd.to_datetime(df.Timestamp + 978307200, unit ='s')

df.to_csv('LteCellLocation.csv')

conn.close()