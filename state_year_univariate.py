import pandas as pd
import numpy
import os

states = ["Alabama", "Alaska", "Arizona", "Arkansas", "BOP", "California", "Colorado",
          "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
          "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
          "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
          "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
          "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
          "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
          "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

important_variables = [
    'custody_49under', 'custody_50to64', 'custody_65over', 'custody_18to24', 'custody_25to44',
    'custody_45to49', 'custody_50plus', 'custody_age_unknown', 'custody_male', 'custody_female',
    'custody_gender_unknown', 'custody_race1_white', 'custody_race1_black', 'custody_race1_latino',
    'custody_race1_other', 'custody_race1_unknown', 'custody_race2_white', 'custody_race2_black',
    'custody_race2_other', 'custody_race2_unknown', 'mortality_49under', 'mortality_50to64',
    'mortality_65over', 'mortality_18to24', 'mortality_25to44', 'mortality_45to49', 'mortality_50plus',
    'mortality_age_unknown', 'mortality_male', 'mortality_female', 'mortality_gender_unknown',
    'mortality_race1_white', 'mortality_race1_black', 'mortality_race1_latino', 'mortality_race1_other',
    'mortality_race1_unknown', 'mortality_race2_white', 'mortality_race2_black', 'mortality_race2_other',
    'mortality_race2_unknown'
]


def state_year_general(state):
    univariate_state_year = pd.read_excel(f"{state}_Univariate.xlsx", 'State-Year')
    raw_state_year = pd.read_excel(f"{state}.xlsx", 'State-Year')
    state_year_pointer = univariate_state_year.fillna('no value')
    raw_state_year_pointer = raw_state_year.fillna('no value')
    years_in_file = (state_year_pointer['year'].tolist())
    year_index = {}
    year_issues = []
    year_unincluded = []
    goodbye = open(f'{state}-State-Year.txt', 'w')
    for years in years_in_file:
        if 2013 <= years <= 2022:
            a_list = state_year_pointer.index[state_year_pointer['year'] == years].tolist()
            for index in a_list:
                year_index.update({years: index})
        elif years < 2013 or years > 2022:
            year_issues.append(years)
    for year in range(2013, 2023):
        if year not in years_in_file:
            year_unincluded.append(year)
    for indexed_year in year_index:
        retrieve_again = year_index.get(indexed_year)
        general_message = univariate_state_year.loc[retrieve_again, 'both_diff']
        message_placeholder = f'{indexed_year}'
        message_placeholder += f" {general_message},"
        for univariate_year in state_year_pointer.columns:
            the_value = state_year_pointer.loc[retrieve_again, univariate_year]
            if the_value != 0 and isinstance(the_value,
                                             numpy.int64) and univariate_year != 'c_age_check_diff' and univariate_year != 'c_all_diff' and univariate_year != 'm_age_check_diff' and univariate_year != 'm_all_diff' and univariate_year != 'year':
                message_placeholder += f' {univariate_year} != 0,'
        for raw_year in raw_state_year_pointer.columns:
            raw_checker = raw_state_year_pointer.loc[retrieve_again, raw_year]
            if raw_checker == 'no value':
                if raw_year == 'custody_tot':
                    message_placeholder += f' NO CUSTODY TOTAL PRESENT.'
                elif raw_year in important_variables:
                    message_placeholder += f' missing {raw_year},'
        print(f'{message_placeholder}\n')
        goodbye.write(f'{message_placeholder}\n\n')
    for second_time in year_issues:
        print(f'{second_time} is included\n')
        goodbye.write(f'{second_time} is included\n\n')
    for third_time in year_unincluded:
        print(f'{third_time} is missing\n')
        goodbye.write(f'{third_time} is missing\n\n')

for individual in states:
    filepath = os.path.join('QC Folder', individual)
    os.chdir(filepath)
    state_year_general(individual)

    os.chdir("/Users/kennny/Desktop/Kenny's QC 2025")
