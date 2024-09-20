# pandas_world_happiness.py

import pandas as pd

scores = pd.read_csv('WHR2023.csv')

print(scores.head(10))
print(len(scores), '# of Countries')

print(scores[scores['Country name'] == 'United States'])