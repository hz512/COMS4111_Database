import pandas as pd
from sqlalchemy import create_engine


engine = create_engine('mysql+pymysql://root:Zhr990512@@localhost/HW4GoT')
df = pd.read_csv(
    "/Users/henryzhu/Documents/GitHub/W4111F20Project/Data/GoT/characters.csv",
    sep=',')
df.to_sql("characters", engine, if_exists='replace', index=False)