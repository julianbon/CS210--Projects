#!/usr/bin/env python
# coding: utf-8

# In[53]:


import math
import re
import numpy as np
import pandas as pd
from collections import defaultdict
from collections import Counter
import matplotlib
from matplotlib import pyplot as plt
def preprocess(f):
    df = pd.read_csv(f) 
    nonedict = {};
   
    for column in df:
        
        
        values = df[column].value_counts().keys().tolist()
        counts = df[column].value_counts().tolist()
        d = dict(zip(values, counts))
        key = "none";
        if key in d:
            nonedict[column] = d[key];        
    sort_nonedict = {k: v for k, v in sorted(nonedict.items(), key=lambda x: x[1], reverse = True)}
    
    i = 0
    for key in sort_nonedict:
        if(i == 3):
            break;
        df.drop(key, inplace=True, axis=1)
        i = i + 1;
    df.replace('\'','', regex=True, inplace=True) 
    
    
    

    df["checking_status"] = np.where(df["checking_status"]=="no checking", "No Checking", df["checking_status"] )
    df["checking_status"] = np.where(df["checking_status"]=="<0", "Low", df["checking_status"] )
    df["checking_status"] = np.where(df["checking_status"]=="0<=X<200", "Medium", df["checking_status"] )
    df["checking_status"] = np.where(df["checking_status"]==">=200", "High", df["checking_status"] )
    
    
    
    df["savings_status"] = np.where(df["savings_status"]=="no known savings", "No Savings", df["savings_status"] )
    df["savings_status"] = np.where(df["savings_status"]=="<100", "Low", df["savings_status"] )
    df["savings_status"] = np.where(df["savings_status"]=="100<=X<500", "Medium", df["savings_status"] )
    df["savings_status"] = np.where(df["savings_status"]=="500<=X<1000", "High", df["savings_status"] )
    df["savings_status"] = np.where(df["savings_status"]==">=1000", "High", df["savings_status"] )
    
    df["class"] = np.where(df["class"]=="good", "1", "0" )
    
    
    
    df["employment"] = np.where(df["employment"]=="unemployed", "Unemployed", df["employment"]) 
    df["employment"] = np.where(df["employment"]=="<1", "Amateur", df["employment"])
    df["employment"] = np.where(df["employment"]=="1<=X<4", "Professional", df["employment"])
    df["employment"] = np.where(df["employment"]=="4<=X<7", "Experienced", df["employment"])
    df["employment"] = np.where(df["employment"]==">=7", "Expert", df["employment"])
    
    
    
    
    df.to_csv("test.csv");
    
   
def analysis(f):
    df = pd.read_csv(f) 
  
    print(pd.crosstab(df["foreign_worker"],df["class"], rownames=[''], colnames=['']))
    
    print(pd.crosstab(df["foreign_worker"],df["savings_status"], rownames=[''], colnames=['']))
    
    averagecredit = df[(df['personal_status'] == "male single" )& (df['employment'] == "Experienced") ]['credit_amount'].mean()
    
    averagecreditduration = df[(df['job'] == "skilled")]['duration'].mean()
                    
    averagecreditduration2 = df[(df['job'] == "unskilled resident")]['duration'].mean()
                                 
                                 
    averagecreditduration3 = df[(df['job'] == "high qualif/self emp/mgmt")]['duration'].mean()   
                                
    averagecreditduration4 = df[(df['job'] == "unemp/unskilled non res")]['duration'].mean()
    
    mostcommonsavingstatus= df[(df['purpose'] == "education")]['savings_status'].mode()  
    
    mostcommoncheckingstatus = df[(df['purpose'] == "education")]['checking_status'].mode()  
    
    print("Most common checking status: " + mostcommoncheckingstatus[0])
    
    print("Most common saving status: " + mostcommonsavingstatus[0])
def visualization(f):
    df = pd.read_csv(f) 
    plt.bar(df['savings_status'], df['personal_status'], color=['black', 'red', 'green', 'blue', 'cyan'])
    plt.show()
    plt.bar(df['checking_status'], df['personal_status'], color=['black', 'red', 'green', 'blue', 'cyan'])
    plt.show()
    
    averageage1 = df[(df['credit_amount'] > 4000 )& (df['property_magnitude'] == "real estate") ]['age'].mean()
    averageage2 = df[(df['credit_amount'] > 4000 )& (df['property_magnitude'] == "life insurance") ]['age'].mean()
    averageage3 = df[(df['credit_amount'] > 4000 )& (df['property_magnitude'] == "no known property") ]['age'].mean()
    averageage4 = df[(df['credit_amount'] > 4000 )& (df['property_magnitude'] == "car") ]['age'].mean()
    
    propmag = ['real estate','life insurance','no known property','car']
    
    list1 = [averageage1,averageage2,averageage3,averageage4]
    
    plt.bar(propmag, list1, color=['black', 'red', 'green', 'blue', 'cyan'])
    plt.show()
    
    personal_stats = ['male div/sep', 'male mar/wid', 'female div/dep/mar','male single']
    mds = len(df[(df['savings_status'] == 'High' )& (df['age'] > 40) & (df['personal_status'] == 'male div/sep' )])
    mdw = len(df[(df['savings_status'] == 'High' )& (df['age'] > 40) & (df['personal_status'] == 'male mar/wid' )])
    fddm = len(df[(df['savings_status'] == 'High' )& (df['age'] > 40) & (df['personal_status'] == 'female div/dep/mar')])
    ms = len(df[(df['savings_status'] == 'High' )& (df['age'] > 40) & (df['personal_status'] == 'male single')])
    
    list2 = [mds,mdw,fddm,ms]
    
    plt.pie(list2, labels = personal_stats)
    
    
    
    plt.show()
    
    
    credithis = ['critical/other existing credit','existing paid','delayed previously','all paid','no credits/all paid']
    
    coec = len(df[(df['savings_status'] == 'High' )& (df['age'] > 40) & (df['credit_history'] == 'critical/other existing credit' )])
    ep = len(df[(df['savings_status'] == 'High' )& (df['age'] > 40) & (df['credit_history'] == 'existing paid' )])
    
    dp = len(df[(df['savings_status'] == 'High' )& (df['age'] > 40) & (df['credit_history'] == 'delayed previously')])
    
    ap = len(df[(df['savings_status'] == 'High' )& (df['age'] > 40) & (df['credit_history'] == 'all paid')])
    
    ncap = len(df[(df['savings_status'] == 'High' )& (df['age'] > 40) & (df['credit_history'] == 'no credits/all paid')])
    
    list3 = [coec,ep,dp,ap,ncap]
    
    
    plt.pie(list3, labels = credithis)
    
    
    plt.show()
    
    
    
    joblist = ['skilled', 'unskilled resident', 'high qualif/self emp/mgmt', 'unemp/unskilled non res']
    
    s = len(df[(df['savings_status'] == 'High' )& (df['age'] > 40) & (df['job'] == 'skilled' )])
    
    us = len(df[(df['savings_status'] == 'High' )& (df['age'] > 40) & (df['job'] == 'unskilled resident')])
    
    hqs = len(df[(df['savings_status'] == 'High' )& (df['age'] > 40) & (df['job'] == 'high qualif/self emp/mgmt')])
    
    uuns = len(df[(df['savings_status'] == 'High' )& (df['age'] > 40) & (df['job'] == 'unemp/unskilled non res')])
    
    
    list4 = [s,us,hqs,uuns]
    
    plt.pie(list4, labels = joblist)
    
    plt.show()
    
    
    
  
 

 
    
    
    
    
    
def main():
  
    preprocess("GermanCredit.csv")
    
    analysis("test.csv");
    
    visualization("test.csv");
    

main()


# In[ ]:





# In[ ]:





# In[ ]:




