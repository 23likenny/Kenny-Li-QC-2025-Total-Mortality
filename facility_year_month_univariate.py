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
          "Vermont", "Virginia", "Washington", "Wisconsin", "Wyoming"]

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
all_months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
master_all_months = set(all_months)


def check_authenticity(state, spreadsheet):
    account_for_both = pd.ExcelFile(f'{state}_Univariate.xlsx')
    if spreadsheet not in account_for_both.sheet_names:
        goodbye = open(f'{state}-Facility-Month.txt', 'w')
        goodbye.write(f'{spreadsheet} DOES NOT EXIST')
        return True
    else:
        return False

def facility_year_month_general(state):
    univariate_facility_year_month = pd.read_excel(f"{state}_Univariate.xlsx", sheet_name='Facility-Month')
    raw_facility_year_month = pd.read_excel(f"{state}.xlsx", sheet_name='Facility-Month')
    univariate_facility_year_month_pointer = univariate_facility_year_month.fillna('no value')
    raw_facility_year_month_pointer = raw_facility_year_month.fillna('no value')
    years_in_file = univariate_facility_year_month_pointer['year'].tolist() #  list of all years, regardless if duplicate
    facilities_in_file = univariate_facility_year_month_pointer['facility_name'].tolist()
    use_for_difference = list(set(univariate_facility_year_month_pointer['facility_name'].tolist()))
    months_in_file = univariate_facility_year_month_pointer['month'].tolist()

    year_issues = []
    year_unincluded = []
    hold_data = {
        2013: {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
            10: [],
            11: [],
            12: []
        },
        2014: {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
            10: [],
            11: [],
            12: []
        },
        2015: {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
            10: [],
            11: [],
            12: []
        },
        2016: {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
            10: [],
            11: [],
            12: []
        },
        2017: {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
            10: [],
            11: [],
            12: []
        },
        2018: {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
            10: [],
            11: [],
            12: []
        },
        2019: {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
            10: [],
            11: [],
            12: []
        },
        2020: {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
            10: [],
            11: [],
            12: []
        },
        2021: {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
            10: [],
            11: [],
            12: []
        },
        2022: {
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
            7: [],
            8: [],
            9: [],
            10: [],
            11: [],
            12: []
        }
    }
    goodbye = open(f'{state}-Facility-Month.txt', 'w')
    first_attempt = enumerate(facilities_in_file)
    clean_version = []
    for index, facility in first_attempt:
        current_year = (univariate_facility_year_month_pointer.loc[index, 'year'])
        current_month = (univariate_facility_year_month_pointer.loc[index, 'month'])
        current_facility = facility
        try:
            if 2013 <= current_year <= 2022:
                hold_data[current_year][current_month].append(current_facility)
                clean_version.append(index)
            elif current_year < 2013 or current_year > 2022:
                year_issues.append(f'{current_facility} for {current_month}/{current_year}')
        except:
            raise Exception(f'Isuse at {current_facility} {current_month}/{current_year} for {state}')
    for year in range(2013, 2023):
        if year not in years_in_file:
            year_unincluded.append(year)
    for individual_year in hold_data:
        for interior_month in hold_data[individual_year]:
            remaining_facilities = set(use_for_difference) - set(hold_data[individual_year][interior_month])
            if len(remaining_facilities) != 0:
                for internally in remaining_facilities:
                    print(f'{internally} for {interior_month}/{individual_year} is missing for {state}')
                    year_unincluded.append(f'{internally} for {interior_month}/{individual_year}')
    for index_again in clean_version:
        current_year_again = univariate_facility_year_month_pointer.loc[index_again, 'year']
        current_month_again = univariate_facility_year_month_pointer.loc[index_again, 'month']
        current_facility_again = univariate_facility_year_month_pointer.loc[index_again, 'facility_name']
        general_message = univariate_facility_year_month_pointer.loc[index_again, 'both_diff']
        message_placeholder = f'{current_month_again}/{current_year_again} for {current_facility_again}'
        message_placeholder += f" {general_message},"
        for univariate_year in univariate_facility_year_month_pointer.columns:
            the_value = univariate_facility_year_month_pointer.loc[index_again, univariate_year]
            if the_value != 0 and isinstance(the_value,
                                             numpy.int64) and univariate_year != 'c_age_check_diff' and univariate_year != 'c_all_diff' and univariate_year != 'm_age_check_diff' and univariate_year != 'm_all_diff' and univariate_year != 'year' and univariate_year != 'month':
                message_placeholder += f' {univariate_year} != 0,'
        for raw_year in raw_facility_year_month_pointer.columns:
            raw_checker = raw_facility_year_month_pointer.loc[index_again, raw_year]
            if raw_checker == 'no value':
                if raw_year == 'custody_tot':
                    message_placeholder += f' NO CUSTODY TOTAL PRESENT.'
                elif raw_year in important_variables:
                    message_placeholder += f' missing {raw_year},'
        goodbye.write(f'{message_placeholder}\n\n')
    for second_time in year_issues:
        goodbye.write(f'{second_time} is included\n\n')
    for third_time in year_unincluded:
        goodbye.write(f'{third_time} is missing\n\n')

for individual in states:
    filepath = os.path.join('QC Folder', individual)
    os.chdir(filepath)
    if check_authenticity(individual, 'Facility-Month'):
        os.chdir("/Users/kennny/Desktop/Kenny's QC 2025")
        print(f'{individual} DOES NOT EXIST')
        continue
    facility_year_month_general(individual)

    os.chdir("/Users/kennny/Desktop/Kenny's QC 2025")
