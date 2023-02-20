import pandas as pd


# Names (keys) mapped to a tuple (the value) containing the height, lat and longitude.
scottish_hills = {'Hill Name': ['Ben Nevis', 'Ben Macdui', 'Braeriach', 'Cairn Toul', 'Sgòr an Lochain Uaine'],
                  'Height': [1345, 1309, 1296, 1291, 1258],
                  'Latitude': [56.79685, 57.070453, 57.078628, 57.054611, 57.057999],
                  'Longitude': [-5.003508, -3.668262, -3.728024, -3.71042, -3.725416]}


dataFrame = pd.DataFrame(scottish_hills, columns=[
                         'Hill Name', 'Longitude', 'Height', 'Latitude'])

#print(dataFrame)
#print(dataFrame.head(2))
#print(dataFrame.tail(2))
# print(dataFrame["Hill Name"])
# print(dataFrame["Height"])
print(dataFrame.Height > 1300)