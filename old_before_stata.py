import pandas as pd

unfilled = pd.read_excel("Alabama.xlsx")
df = unfilled.fillna(0)

custody_total_2013 = (df.loc[0, 'custody_tot'])
custody_total_2014 = (df.loc[1, 'custody_tot'])
custody_total_2015 = (df.loc[2, 'custody_tot'])
custody_total_2016 = (df.loc[3, 'custody_tot'])
custody_total_2017 = (df.loc[4, 'custody_tot'])
custody_total_2018 = (df.loc[5, 'custody_tot'])
custody_total_2019 = (df.loc[6, 'custody_tot'])
custody_total_2020 = (df.loc[7, 'custody_tot'])
custody_total_2021 = (df.loc[8, 'custody_tot'])
custody_total_2022 = (df.loc[9, 'custody_tot'])
def ages():
    for i in range(0, 1):
        print(
            f'custody_diff_age_type1: {int(custody_total_2013) - int(df.loc[i, 'custody_49under']) - int(df.loc[i, 'custody_50plus']) - int(df.loc[i, 'custody_age_unknown'])}')
        print(
            f'custody_diff_age_type2: {int(custody_total_2013) - int(df.loc[i, 'custody_49under']) - int(df.loc[i, 'custody_50to64']) - int(df.loc[i, 'custody_65over']) - int(df.loc[i, 'custody_age_unknown'])}')
        print(
            f'custody_diff_age_type3: {int(custody_total_2013) - int(df.loc[i, 'custody_18to24']) - int(df.loc[i, 'custody_25to44']) - int(df.loc[i, 'custody_45to49']) - int(df.loc[i, 'custody_50to64']) - int(df.loc[i, 'custody_65over']) - int(df.loc[i, 'custody_age_unknown'])}')
        print(
            f'custody_diff_age_type4: {int(custody_total_2013) - int(df.loc[i, 'custody_18to24']) - int(df.loc[i, 'custody_25to44']) - int(df.loc[i, 'custody_45to49']) - int(df.loc[i, 'custody_50plus']) - int(df.loc[i, 'custody_age_unknown'])}')
        print(
            f'custody_diff_age_type5: {int(custody_total_2013) - int(df.loc[i, 'custody_18to24']) - int(df.loc[i, 'custody_25to49']) - int(df.loc[i, 'custody_50to64']) - int(df.loc[i, 'custody_65over']) - int(df.loc[i, 'custody_age_unknown'])}')
        print(
            f'custody_diff_age_type6: {int(custody_total_2013) - int(df.loc[i, 'custody_18to24']) - int(df.loc[i, 'custody_25to49']) - int(df.loc[i, 'custody_50plus']) - int(df.loc[i, 'custody_age_unknown'])}')

def genders():
    for i in range(0, 1):
        print(f'custody_diff_gender: {int(custody_total_2013) - int(df.loc[i, 'custody_male']) - int(df.loc[i, 'custody_female']) - int(df.loc[i, 'custody_gender_unknown'])}')
def race1():
    for i in range(0, 1):
        print(f'custody_diff_gender: {int(custody_total_2013) - int(df.loc[i, 'custody_race1_white']) - int(df.loc[i, 'custody_race1_black']) - int(df.loc[i, 'custody_race1_latino']) - int(df.loc[i, 'custody_race1_other']) - int(df.loc[i, 'custody_race1_unknown'])}')
def race2():
    for i in range(0, 1):
        print(f'custody_diff_gender: {int(custody_total_2013) - int(df.loc[i, 'custody_race2_white']) - int(df.loc[i, 'custody_race2_black']) - int(df.loc[i, 'custody_race2_other']) - int(df.loc[i, 'custody_race2_unknown'])}')
