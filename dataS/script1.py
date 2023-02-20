import pandas as pd

dataframe = pd.read_csv("scottish_hills.csv")

# print(dataframe.head(10))

# sorted_hills = dataframe.sort_values(by=['Height'], ascending=False)
# sorted_hills = dataframe["Hill Name"]
sorted_hills = dataframe.iloc[0]

print(sorted_hills)