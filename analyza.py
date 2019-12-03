#%%
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# %%
data_volby = pd.read_excel("./data/parlgov.xlsx", sheet_name="election")
data_party = pd.read_excel("./data/parlgov.xlsx", sheet_name="party")

# %%
print(data_volby.columns)
print(data_party.columns)
# %%
data = data_volby.merge(data_party, on="party_id", how="left")
# %%
chci=["Social democracy", "Conservative", "Liberal", "Communist/Socialist", "Christian democracy", "Agrarian", "Green/Ecologist"]
data_filter=data[ (data.election_type=="parliament") & (data.election_date >= "1990-01-01" ) & (data.family_name.isin(chci))] 

# %%
for country in data_filter.country_name_x.unique():
    data_country = data_filter[ data_filter.country_name_x == country ]
    #nakresli graf


# %%
