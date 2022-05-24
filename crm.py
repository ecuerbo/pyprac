import pandas as pd
import seaborn as sns

crm = pd.read_csv("data/crm.csv", index_col="DT", parse_dates=True)

#crm.head()

sns.boxplot(x='sample',y='ni',hue='xrf',data=crm)