import pandas as pd

athlete_data = pd.read_csv('files/athlete_events.csv')
athlete_data['Height_Category'] = athlete_data['Height'].apply(lambda x: "Short" if x < 165 else ("Average" if x < 185 else "Tall"))

def categorize_athlete(row):
  if row["Height"] < 175 and row["Weight"] < 70:
    return "Lightweight"
  elif row["Height"] < 185 or row["Weight"] <= 80:
    return "Midweight"
  else:
    return "Heavyweight"
  
athlete_data["Athlete_Category"] = athlete_data.apply(categorize_athlete, axis=1)
print(athlete_data[["Height_Category", "Athlete_Category"]].head())