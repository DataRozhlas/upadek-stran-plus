#%%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

# %%
data_volby = pd.read_excel("./data/parlgov.xlsx", sheet_name="election")
data_party = pd.read_excel("./data/parlgov.xlsx", sheet_name="party")

# %%
data = data_volby.merge(data_party[['party_id', 'family_name']], on="party_id", how="left")
#%%
data.election_date = pd.to_datetime(data.election_date, format='%Y-%m-%d')

#%%
data['election_year'] = data.election_date.apply(lambda x: int(str(x).split('-')[0]))

#%%
chci=["Social democracy", "Conservative", "Liberal", "Communist/Socialist", "Christian democracy", "Agrarian", "Green/Ecologist"]
# %%
data = data[ (data.election_type == "parliament") & (data.election_year >= 1990 )] 

#%%

#%%
graph_data = []
for family in data.family_name.unique():
    family_data = []
    for year in sorted(list(data.election_year.unique())):
        tmp = data[ (data.election_year == year) & (data.family_name == family) ]
        if tmp.vote_share.median() != tmp.vote_share.median():
            family_data.append(0)
        else:
            family_data.append(tmp.vote_share.median())
    graph_data.append(family_data)

#%%
plt.stackplot(sorted(list(data.election_year.unique())), graph_data, labels=list(data.family_name.unique()))
plt.legend(loc='upper left')
plt.show()

# %%
