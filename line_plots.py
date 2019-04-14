# %% libraries and data
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# %% Make a sample data frame for testing
#df=pd.DataFrame({'x': range(1,11), 'y1': np.random.randn(10), 'y2': np.random.randn(10)+range(1,11), 'y3': np.random.randn(10)+range(11,21), 'y4': np.random.randn(10)+range(6,16), 'y5': np.random.randn(10)+range(4,14)+(0,0,0,0,0,0,0,-3,-8,-6), 'y6': np.random.randn(10)+range(2,12), 'y7': np.random.randn(10)+range(5,15), 'y8': np.random.randn(10)+range(4,14), 'y9': np.random.randn(10)+range(4,14) })
#df.head()

# %% Plot cohort data as a function of time
cohort_ed = 'Some College'
cohort_gender = 'Male'
cohort_income = '$70,000 - $74,999'
cohort_age = '65-74 years old'

# Import data and focus on key values and prevalances
df_std = pd.read_csv('oldpplCA.csv')
df_key = df_std[['age','gender','state','income','education','date','chlamydia',\
    'gential_warts','gonorrhea','herpes','hpv','other_std','parasitic','syphilis','trich']]
#df_key['income'].value_counts()

# %% Print total number of nans
print(df_key.isna().sum().sum())

# %% Find income bracket with the most recorded data
min = 100000
income_dict = {}
for income_bracket in df_key['income'].unique():
    num_nans = df_key[df_key['income']==income_bracket].isna().sum().sum()
    if (num_nans < min):
        min = num_nans
        min_income_bracket = income_bracket
    income_dict[income_bracket] = num_nans

for key, value in sorted(income_dict.items(), key=lambda item: item[1]):
    print("%s: %s" % (key, value))

# %% Find education level with the most recorded data
min = 100000
education_dict = {}
for education_bracket in df_key['education'].unique():
    num_nans = df_key[df_key['education']==education_bracket].isna().sum().sum()
    if (num_nans < min):
        min = num_nans
        min_education_bracket = education_bracket
    education_dict[education_bracket] = num_nans

for key, value in sorted(education_dict.items(), key=lambda item: item[1]):
    print("%s: %s" % (key, value))


# %% Find gender with the most recorded data
min = 100000
gender_dict = {}
for gender_bracket in df_key['gender'].unique():
    num_nans = df_key[df_key['gender']==gender_bracket].isna().sum().sum()
    if (num_nans < min):
        min = num_nans
        min_gender_bracket = gender_bracket
    gender_dict[gender_bracket] = num_nans

for key, value in sorted(gender_dict.items(), key=lambda item: item[1]):
    print("%s: %s" % (key, value))


# %% Find age group with the most recorded data
min = 100000
age_dict = {}
for age_bracket in df_key['age'].unique():
    num_nans = df_key[df_key['age']==age_bracket].isna().sum().sum()
    if (num_nans < min):
        min = num_nans
        min_age_bracket = age_bracket
    age_dict[age_bracket] = num_nans

for key, value in sorted(age_dict.items(), key=lambda item: item[1]):
    print("%s: %s" % (key, value))


# %% Focus on particular cohort
df_red = df_key[(df_key['gender']==cohort_gender) & (df_key['age']==cohort_age) \
    & (df_key['education']==cohort_ed) & (df_key['income']==cohort_income)]
df_red = df_red.drop(['age', 'gender','state','education','income'], axis=1)
df_red['date'] = pd.to_datetime(df_red.date)
df_red = df_red.sort_values(by='date',ascending=True)

# display resulting cohort
#df_red.head(20)

# %% Initialize the figure
plt.figure(figsize=(10,10))
plt.style.use('seaborn-darkgrid')

# create a color palette
palette = plt.get_cmap('Set1')

# multiple line plot
num=0
for column in df_red.drop('date', axis=1):
    num+=1
    plot_df = df_red[np.isfinite(df_red[column])]
    x = plot_df['date']
    y = plot_df[column]

    # Find the right spot on the plot
    plt.subplot(3,3, num)

    # plot every groups, but discreet
    for v in df_red.drop('date', axis=1):
        other_df = df_red[np.isfinite(df_red[v])]
        other_x = other_df['date']
        other_y = other_df[v]

        plt.plot(other_x, other_y, marker='', color='grey', linewidth=0.6, alpha=0.3)

    # Plot the lineplot
    plt.plot(x,y, marker='', color=palette(num), linewidth=2.4, alpha=0.9, label=column)

    # Same limits for everybody!
    # plt.xlim(0,10)
    # plt.ylim(-2,22)

    # Not ticks everywhere
    # if num in range(7) :
    #     plt.tick_params(labelbottom=False)
    # if num not in [1,4,7] :
    #     plt.tick_params(labelleft=False)

    # Add title
    plt.title(column, loc='left', fontsize=12, fontweight=0, color=palette(num) )

plt.savefig(('stds_most_sampled_' + cohort_gender + '.png'))

# general title
# plt.suptitle("hi how are you")
#plt.suptitle("How the 9 students improved\nthese past few days?", fontsize=13, fontweight=0, color='black', style='italic', y=1.02)

# %% Axis title
# plt.text(0.06, 0.5, 'Note', ha='center', va='center', rotation='vertical')


# %% Which STD has the most data?
print(df_key.isna().sum())

# %% Focus on herpes since it has least amount of NaNs
df_red = df_key[(df_key['gender']==cohort_gender) & (df_key['age']==cohort_age) \
    & (df_key['income']==cohort_income)]
df_red = df_red.drop(['age', 'gender','state','income','chlamydia',\
    'gential_warts','gonorrhea','hpv','other_std','parasitic',\
    'syphilis','trich'], axis=1)
df_red['date'] = pd.to_datetime(df_red.date)
df_red = df_red.sort_values(by='date',ascending=True)
df_red = df_red[np.isfinite(df_red['herpes'])]
df_red.head()

# %% Plot herpes for different education (given certian income)
fig, ax = plt.subplots(figsize=(10,10))

for key, grp in df_red.groupby(['education']):
    ax = grp.plot(ax=ax, kind='line', x='date', y='herpes', label=key,fontsize=16)

plt.legend(loc='best',fontsize = 12)
plt.xlabel('Date',fontsize=16)
plt.ylabel('Prevalance (Herpes)',fontsize=16)
plt.title(cohort_gender,fontsize=16)
plt.savefig(('herpes_vs_time_' + cohort_gender + '.png'))
plt.show()

# %%
#print(df_std.columns)
# df_std['entertainment_movies_spend'].describe()
# df_std['entertainment_movies_spend'].hist()
df_std.entertainment_movies_spend.value_counts().plot(kind='bar')
