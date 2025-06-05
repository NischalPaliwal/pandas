import pandas as pd

nocs = pd.read_csv('files/noc_regions.csv')
bios = pd.read_csv('files/athlete_events.csv')

merged = pd.merge(bios, nocs, on='NOC', how='inner')
