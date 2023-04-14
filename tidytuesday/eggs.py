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

#let's get the type of the columns
eggs_df.dtypes

#ok, let's parse the observed_month to a date
eggs_df['date'] = pd.to_datetime(eggs_df['observed_month'], format='%Y-%m-%d')

#confirm this worked
eggs_df.dtypes
#ok cool

#and what if we want to get the month from each date?
eggs_df['month'] = eggs_df['date'].dt.month
eggs_df['year'] = eggs_df['date'].dt.year

#and let's get the avg eggs per month
month_mean = eggs_df.groupby('month')['n_eggs'].mean().reset_index()

month_mean