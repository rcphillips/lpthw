# Import the necessary packages
# known
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
# This just makes it look like R. What's up with these R folks...
plt.style.use('ggplot')

# Where to save the figures

datapath = Path.home() / "Desktop/lpthw/projects/DavisSML_lect1/data"
print(datapath)

# loads the file. Don't forget that windows can't figure out when you say .csv
# in your file name, that you don't want .csv.csv...
oecd_bli = pd.read_csv(datapath / "oecd_bli_2015.csv", thousands=',')  # some 
# sort of delimiter?

oecd_bli = oecd_bli[oecd_bli["INEQUALITY"] == "TOT"]  # column relabling
# print(oecd_bli.head())
# what does pivoting do?
# also note we're recreating what oecd_bli is
oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")
# our pivot here examines column "indicator" and expands it out for each entry
# in indicator, making 24 columns. All other columns are dropped, too.
# meanwhile, the rows are established (the index is established) by the
# country column. Finally, the values are pulled from the country-indicator
# values of the original table.
oecd_bli.head()
# print(oecd_bli.head())

print(oecd_bli.columns)

# head of just one column, the column we'll take as an output.
print(oecd_bli["Life satisfaction"].head())
# getting the next csv.
gdp_per_capita = pd.read_csv(
				datapath / "gdp_per_capita.csv",
				thousands=',',
				delimiter='\t',
				encoding='latin1',
				na_values="n/a"
				)
# renaming some columns
gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
gdp_per_capita
print(gdp_per_capita.head())

# merge is pandas for join. defaults to inner join. the indexes can be used as
# join keys? Ah, and we've rewritten our tables such that the indices are both
# country names.

full_country_stats = pd.merge(
					left=oecd_bli, 
					right=gdp_per_capita, 
					left_index=True,
					right_index=True
					)
# sorting the values so that highest gdp is up top
full_country_stats.sort_values(by="GDP per capita", inplace=True)
print(full_country_stats.head())