#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

# %%
data_volby = pd.read_excel("./data/parlgov.xlsx", sheet_name="election")
data_party = pd.read_excel("./data/parlgov.xlsx", sheet_name="party")

#%%
# %%
data = data_volby.merge(data_party[['party_id', 'family_name']], on="party_id", how="left")
#%%
data.election_date = pd.to_datetime(data.election_date, format='%Y-%m-%d')

#%%
data['election_year'] = data.election_date.apply(lambda x: int(str(x).split('-')[0]))

#%%
chci=["Social democracy"]
staty = ['Austria', 'Czech Republic', 'Germany', 'France', 'Hungary', 'Poland', 'Slovakia', 'Sweden', 'Netherlands']

data = data[ (data.election_type == "parliament") & (data.election_year >= 1990 ) & data.family_name.isin(chci) & data.country_name.isin(staty)] 

#%%
for country in sorted(list(data.country_name.unique())):
    tmp = data[data.country_name == country]
    chrt = sns.lineplot(x="election_year", y="vote_share", hue="family_name", data=tmp, ci=None)
    chrt.set_title(country)
    plt.legend(loc='upper left')
    plt.show()