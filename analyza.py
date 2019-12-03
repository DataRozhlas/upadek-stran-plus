#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

# %%
data_volby = pd.read_excel("./data/parlgov.xlsx", sheet_name="election")
data_party = pd.read_excel("./data/parlgov.xlsx", sheet_name="party")

# %%
data = data_volby.merge(data_party, on="party_id", how="left")
#%%
data.election_date = pd.to_datetime(data.election_date, format='%Y-%m-%d')

#%%
data.columns
# %%
chci=["Social democracy", "Conservative", "Liberal", "Communist/Socialist", "Christian democracy", "Agrarian", "Green/Ecologist"]
data_filter=data[ (data.election_type == "parliament") & (data.election_date >= "1990-01-01" ) & (data.family_name.isin(chci))] 

#%%
data_filter.sort_values(by='election_date', inplace=True)
data_filter = data_filter[data_filter.vote_share.values >= 5]

# %%
for country in data_filter.country_name_x.unique():
    data_country = data_filter[ data_filter.country_name_x == country ]
    chrt = sns.lineplot(x='election_date', y='vote_share', data=data_country, hue='family_name', ci=None)
    chrt.set_title(country)
    plt.show()
