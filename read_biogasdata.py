import pandas as pd
import numpy as np

df = pd.read_csv('CleanData/HainanData_kindofClean.csv')
df.head()

# Input Columns? Arbitrarily separate at col 8 for testing. Nothing is actually done at this step.
df.head().iloc[:,0:8] 
df.head().iloc[:,9:]

# Create d2 which will be a timeshifted dataframe
d2 = df

# Set number of time shift days
time_shift = 10

#time shift the output dataframe columns and save in place to d2. 
# The cells that went up past the initial row are automatically deleted.
d2.iloc[:,9:] = df.iloc[:,9:].shift(-time_shift)

# Drop the rows at the bottom
df.drop(df.tail(time_shift).index,inplace=True)

d2