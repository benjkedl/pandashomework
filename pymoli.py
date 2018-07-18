#dependancies

import pandas as pd 
import numpy as np 

purchase = pd.read_csv('purchase_data.csv', delimiter=',')

#total player number
players = purchase.loc[:,'SN'].unique()
playernum = len(players)

#make function for age & gender analysis
def genderanalysis(gender):
    global playernum
    gcount = len(gender['SN'].unique())
    gpercent = round(gcount/playernum *100, 2)
    count = gender.shape[0]
    avg = round(gender['Price'].mean(), 2)
    total = gender['Price'].sum()
    avgper_df = gender.pivot_table(index='SN', values='Price', aggfunc=sum)
    avgper = round(avgper_df.values.mean(), 2)
    return {'Player_Count': gcount, 'Player_Percent': gpercent, 'Purchase_Count': count, 
            'Average_Purchase_Price': avg, 'Total_Purchase_Value': total, 'Average_Purchase_Total': avgper}

#group by gender
male = purchase.loc[purchase['Gender'] == 'Male', :]
female = purchase.loc[purchase['Gender'] == 'Female',:]
othergen = purchase.loc[purchase['Gender'] == 'Other / Non-Disclosed', :]

#group by age (binning)
bins = [0,10,14,18,22,26,30,34,38,42,46]
bin_lab =['<10', '10-14', '14-18', '18-22', '22-26', '26-30', '30-34', '34-38',
        '38-42', '42-46']
purchase['Age Group'] = pd.cut(purchase['Age'], bins, labels=bin_lab)

#analyze with function, both gender and age
male_analysis = genderanalysis(male)
female_analysis = genderanalysis(female)
other_analysis = genderanalysis(othergen)

age_df = pd.DataFrame([],columns=bin_lab)

for label in bin_lab:
    agegroup = purchase.loc[purchase['Age Group'] == label, :]
    age_analyzed = genderanalysis(agegroup)
    age_df[label] = age_analyzed

    

print(male_analysis)

age_df


