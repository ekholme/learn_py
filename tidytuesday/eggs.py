import pandas as pd
import numpy as np

url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2023/2023-04-11/egg-production.csv"
eggs_df = pd.read_csv(url)

#view head
eggs_df.head()

#will return descriptives of numerical cols
eggs_df.describe()

#get dimensions
eggs_df.shape
#ok, so we have a 220 by 6 df

np.corrcoef(eggs_df['n_hens'], eggs_df['n_eggs'])
#ok so these are incredibly highly correlated

