import pandas as pd
import numpy as np

wells = pd.read_csv('./../dat/well-data-orig.csv')
wells["FUNC"][wells.FUNC == "no"] = "No"
# Extract year from report date
wells.RPT_DATE = pd.to_datetime(wells.RPT_DATE)
wells["RPT_YEAR"] = wells.RPT_DATE.dt.year
wells.RPT_YEAR.value_counts()  # See how many records per year we have

# Select only wells with report years in [2001, 2015]
df = wells[wells.RPT_YEAR > 2000]
df = df[df.RPT_YEAR < 2016]
# Remove water source if it is rain-fed. Need to make sure there are no
# NA values for this to work
df["WATERSRC"] = df["WATERSRC"].fillna("Not recorded")
df = df[~df["WATERSRC"].str.contains("^rain", case=False)]
# There is a small set of "WATERTECH" entries that are
# rainwater collection. Get rid of these too.
df["WATERTECH"] = df["WATERTECH"].fillna("Not recorded")
df = df[~df["WATERTECH"].str.contains("^rain", case=False)]

# Extract "Breakdown year" from "STATUS" column
df["STATUS"] = df["STATUS"].fillna("Not recorded")
df["BKDWN_YEAR"] = df["STATUS"].str.extract("(\d{4,})")
# If there is no breakdown data, assume that breakdown (if FUNC=="No")
# occurs during the RPT_YEAR
no_bkdwn = df.BKDWN_YEAR.isnull()
df["BKDWN_YEAR"][no_bkdwn] = df["RPT_YEAR"][no_bkdwn]

LL = (26., -4.)  # Lower left corner of bounding box.
UR = (44., 13.)  # Upper right corner of bounding box
df = df[(df.LAT_DD > LL[1]) & (df.LAT_DD < UR[1]) &
        (df.LONG_DD > LL[0]) & (df.LONG_DD < UR[0])]

# # Write this modified data to a new CSV file.
df.to_csv('./../dat/well-data-2001-2015-no-rainwater-clipped.csv', index=False)
