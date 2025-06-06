import pandas as pd

bios = pd.read_csv('files/athlete_events.csv')
print(bios['City'].value_counts())