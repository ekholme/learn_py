import numpy as np
import polars as pl

#practicing using polars
marathon = pl.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2023/2023-04-25/london_marathon.csv')
winners = pl.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2023/2023-04-25/winners.csv')

#looking at winners
winners.head()

#looking at range of years
years = winners.select(
    pl.col("Year").unique().alias("unique_years")
)

#writing a little helper function to convert time
def get_time(time_string):
    h, m, s = time_string.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

#Parse time in seconds
winners = winners.with_columns(
    pl.col("Time").apply(get_time).alias("Time_Seconds")
)

