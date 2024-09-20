import pandas as pd

df = pd.DataFrame({
        'Data': {0:1, 1:9, 2:14, 3:19},
        'Weight': {0:2, 1:3, 2:1, 3:7}
        },
    columns=['Data', 'Weight']
)

print(df.head())

weightedMean = (1*2 + 9*3 + 14*1) / (2+3+1)
print(weightedMean)

wm_formula = (df['Data'] * df['Weight']).sum() / df['Weight'].sum()
print(wm_formula)