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
# druhy graf cesko
x = data[(data.country_name_short == 'CZE') & (data.election_year >= 1996) & (data.election_type == "parliament")]

xd = pd.DataFrame(x.groupby(['election_year', 'family_name']).vote_share.sum().reset_index())

#%%
xd
#%%
family_cze = {'Christian democracy': 'křesťanská demokracie',
'Communist/Socialist': 'komunisti',
'Conservative': 'konzervativci',
'Liberal': 'liberálové',
'Right-wing': 'pravice',
'Social democracy': 'sociální demokracie',
'Green/Ecologist': 'zelení',
'Special issue': 'jedno téma'}

out = []
for party in xd.family_name.unique():
    tmp = xd[xd.family_name == party]
    out.append({
        'name': family_cze[party],
        'data': list(map(lambda x: [x[0], x[2]], tmp.values)),
        'step': 'right'
    })

#%%
pd.DataFrame(data[(data.election_type == "parliament") & (data.election_year >= 1996 ) & (data.country_name_short == 'CZE')].groupby('family_name').party_name.unique()).to_dict()

#%%
chci=["Social democracy"]
staty = ['Czech Republic', 'Germany', 'France', 'Hungary', 'Poland', 'Slovakia', 'Sweden', 'Netherlands']
staty_cze = ['Česká republika', 'Německo', 'Francie', 'Maďarsko', 'Polsko', 'Slovensko', 'Švédsko', 'Nizozemsko']

staty_trans = dict(zip(staty, staty_cze))

data = data[ (data.election_type == "parliament") & (data.election_year >= 1996 ) & data.family_name.isin(chci) & data.country_name.isin(staty)] 

#%%
for country in sorted(list(data.country_name.unique())):
    tmp = data[data.country_name == country]
    chrt = sns.lineplot(x="election_year", y="vote_share", hue="family_name", data=tmp, ci=None)
    chrt.set_title(country)
    plt.legend(loc='upper left')
    plt.show()

#%%
d = pd.DataFrame(data.groupby(['country_name', 'election_year']).vote_share.sum().reset_index())

# %%
out = []
for cntry in d.country_name.unique():
    tmp = d[d.country_name == cntry]
    out.append({
        'name': staty_trans[cntry],
        'data': list(map(lambda x: [x[1], x[2]], tmp.values)),
        'step': 'right'
    })