import pandas as pd
import numpy as np
import sys
# %%

df=pd.read_csv('oldpplCA.csv')
df.head()

# %%

#get all columns with categorial variables
obj_df=df.select_dtypes(include=['object']).copy()
obj_df=obj_df.drop('date',axis=1)
string_cols=obj_df.columns
string_cols=list(string_cols)
print(string_cols)

# %%
#one-hot encoding for these
final_df=pd.concat([df,pd.get_dummies(df[string_cols])],axis=1)
#convert dates to datetimes
final_df['date']=final_df['date'].astype('datetime64[ns]')
print(list(final_df.columns))
print(list(final_df.dtypes))

# %%



# %%
#multiple regression on each std
#get lists of dependent and independent variables
import statsmodels.api as sm

#dependent vars
std_list=['chlamydia','gential_warts','gonorrhea','herpes','hpv',
          'other_std','parasitic','syphilis','trich']

#independent vars
age_vars=['age_65-74 years old','age_75+ years old']
gender_vars=['gender_Female','gender_Male']
income_vars=list(final_df['income'].unique())
for i in range(len(income_vars)):
    temp=income_vars[i]
    temp2='income_'+temp
    income_vars[i]=temp2
education_vars=list(final_df['education'].unique())
for i in range(len(education_vars)):
    temp=education_vars[i]
    temp2='education_'+temp
    education_vars[i]=temp2

# %%
import numpy as np
total_list=list(income_vars+education_vars+gender_vars)
arr=np.array(np.zeros((len(std_list),len(total_list))))

for i in range(len(std_list)):
    std=std_list[i]
    y=final_df[std]
    X=final_df[gender_vars+income_vars+education_vars]
    est=sm.OLS(y,X,missing='drop').fit()
    arr[i,:]=est.pvalues
    #print(est.summary()
for i in range(len(std_list)):
    std=std_list[i]
    for j in range(len(total_list)):
        var=total_list[j]
        print('\t'+ std + '\t'+var+ '\t'+ str(arr[i,j]))
alpha=0.05
bonferroni_p=alpha/len(list(income_vars+education_vars+gender_vars))
print(bonferroni_p)
