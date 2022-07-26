
# We use the library pandas to import the data from the datasets

import pandas as pd

trades = pd.read_csv(r"C:\Users\Alex\Desktop\interview\Client trades.txt",sep = "\t", header = 0)

list_trades = trades.values.tolist()

#trades = trades.drop([x for x in range(3424,1048575)])

print(trades.head())
print("")

print(trades.tail())



balances = pd.read_csv(r"C:\Users\Alex\Desktop\interview\Client balances.csv",sep = "\t", header = 0)



balances = balances.drop([x for x in range(16071,1048575)])
list_balances = balances.values.tolist()


print(balances.head())
print("")

print(balances.tail())



balance_usd = []

for i in range(len(list_balances)):
    balance_usd.append(list_balances[i][3])


# bal = [""]*len(balance_usd)
# for i in range(len(balance_usd)):
#     for char in balance_usd[i]:
#         if char in symbols:
#             bal[i]+=char
            

rates = pd.read_csv(r"C:\Users\Alex\Desktop\interview\rates.txt",sep = "\t", header = 0)

rates = rates.drop("Unnamed: 3",1)
list_rates = rates.values.tolist()
inv_euro = []



symbols = "0123456789.-("

profit = []

for i in range(len(list_trades)):
    profit.append(list_trades[i][8])
    
prof = [""]*len(profit)
for i in range(len(profit)):
    for char in profit[i]:
        if char in symbols:
            prof[i]+=char

# We clean the data

prof2 = [""]*len(prof)
for i in range(len(prof)):
    if prof[i][0] == "-":
        item = "0"
        prof2[i] = item
    elif prof[i][0] == "(":
        item = "-"
        for j in range(1,len(prof[i])):
            item+=prof[i][j]
        prof2[i] = item
    else:
        prof2[i] = prof[i]


# testing 
# for i in range(100):
#     print(prof[i],"****",prof2[i])
                


for i in range(len(prof2)):
    prof2[i] = float(prof2[i])



for i in range(len(list_trades)):
    list_trades[i][8] = prof2[i]

        

clients = []
for i in range(len(list_trades)):
    clients.append(list_trades[i][1])
   
sclients = set(clients)
lclients = list(sclients)

currencies = []
euro_rates = []


for i in range(len(list_rates)):
    currencies.append(list_rates[i][0])
    euro_rates.append(list_rates[i][2])

            

cur = []
for i in range(len(list_trades)):
    cur.append(list_trades[i][10])


for i in range(len(clients)):
    for j in range(len(euro_rates)):
        if cur[i] == currencies[j]:
            inv_euro.append(euro_rates[j])


# We multiply the profit of the clients with the corresponding rate

counter_clients = [0]*len(lclients)

for i in range(len(clients)):
    for j in range(len(lclients)):
        if clients[i] == lclients[j]:
            counter_clients[j] += prof2[i]*inv_euro[i]
            
# We find the total profit per client


total_profit_per_client = []
for i in range(len(lclients)):
    total_profit_per_client.append([lclients[i],counter_clients[i]])



date = []
commission = []
for i in range(len(list_trades)):
    date.append(list_trades[i][2])
    commission.append(list_trades[i][6])

date1 = []
for i in range(len(date)):
    date1.append(int(date[i][0]+date[i][1]))

sdate1 = set(date1)


sdate1 = set(date1)
ldate1 = list(sdate1)
count_dates = [0]*len(sdate1)

for i in range(len(date)):
    for j in range(len(ldate1)):
        if date1[i] == ldate1[j]:
            count_dates[j] += abs(commission[i])          
            
            
# We find the client with the biggest losses            
            
min = total_profit_per_client[0][1]
loser = total_profit_per_client[0][0]

for i in range(len(total_profit_per_client)):
    if total_profit_per_client[i][1] < min:
        min = total_profit_per_client[i][1]
        loser = total_profit_per_client[i][0]


# We find the most traded asset

asset = []
for i in range(len(list_trades)):
    asset.append(list_trades[i][5])


sasset = set(asset)
lasset = list(sasset)


c_asset_trades = [0]*len(lasset)

for i in range(len(asset)):
    for j in range(len(lasset)):
        if asset[i] == lasset[j]:
            c_asset_trades[j]+=1



max = c_asset_trades[0]
most_traded_asset = lasset[0]
for i in range(len(c_asset_trades)):
    if c_asset_trades[i]>max:
        max = c_asset_trades[i]
        most_traded_asset = lasset[j]


# We find the most losing asset

column=[0]*len(inv_euro)
for i in range(len(prof2)):
    column[i] = prof2[i]*inv_euro[i]

profit = [0]*len(lasset)
for i in range(len(asset)):
    for j in range(len(lasset)):
        if asset[i] == lasset[j]:
            profit[j]+=column[i]



profit_min = profit[0]
asset_min = lasset[0]
for i in range(len(profit)):
    if profit[i] < profit_min:
        profit_min = profit[i]
        asset_min = lasset[i]
        
        
        
# Data visualisation, Balance per country

import pandas as pd

import matplotlib.pyplot as plt     
        
df = pd.read_csv(r"C:\Users\Alex\Desktop\interview\BalancePerCountry.txt")
        
data = df.values.tolist()
    
countries = []
balance = []

for i in range(len(data)): 
    countries.append(data[i][0])
    balance.append(int(data[i][1]))
    
total_balance = 0
for i in range(len(balance)):
    total_balance += balance[i]
        

t_b = [x/total_balance for x in balance]     
        
        
labels = "Canada","Cyprus","Czech Rebulic","France","Greece","Hungary","Italy","UK"
sizes = t_b
explode = (0, 0, 0, 0.1, 0.1, 0, 0, 0.1)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=180)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Balance percentage per country")
plt.show()
        


# Data visualisation, Balance per group


import pandas as pd

import matplotlib.pyplot as plt     
        
df = pd.read_csv(r"C:\Users\Alex\Desktop\interview\BalancePerGroup.txt")
        
data = df.values.tolist()

group = []
balance = []

for i in range(len(data)): 
    group.append(data[i][0])
    balance.append(int(data[i][1]))
    
total_balance = 0
for i in range(len(balance)):
    total_balance += balance[i]
        

t_b = [x/total_balance for x in balance]     
#for i in range(len(balance)):
    
        
labels = "Gold","Platinum","Regular","VIP"
sizes = t_b
explode = (0, 0, 0, 0.1)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=180)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Balance percentage per group")
plt.show()
        
        
#%%


# with open("clients.txt","w") as file:
#     for i in range(len(prof2)):
#         file.write(str(clients[i]) + "," 
#                    + str(date[i]) +  ","          
#                    + str(asset[i]) + ","
#                    + str(prof2[i]) + ","
#                    +   "\n")
        

# with open("rates.txt", "w") as file:
#     for i in range(len(rates)):
#         file.write(int(rates[i]))
        
        
        
#print(r"Hello\nAlex")        
        
        
        
        
        
        
        
        
        
        
        