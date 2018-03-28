## 4. Reading in the Data ##

import pandas as pd
data_files = [
    "ap_2010.csv",
    "class_size.csv",
    "demographics.csv",
    "graduation.csv",
    "hs_directory.csv",
    "sat_results.csv"
]
data = {}

for file in data_files:
    base = file.split('.')[0]
    path = 'schools/' + file
    data[base] = pd.read_csv(path)

## 5. Exploring the SAT Data ##

data['sat_results'].head(5)

## 6. Exploring the Remaining Data ##

for db in data.values():
    print(db.head(5))

## 8. Reading in the Survey Data ##

all_survey = pd.read_csv('schools/survey_all.txt', delimiter='\t', encoding='windows-1252')
d75_survey = pd.read_csv('schools/survey_d75.txt', delimiter='\t', encoding='windows-1252')

survey = pd.concat([all_survey, d75_survey], axis=0)

survey.head(5)

## 9. Cleaning Up the Surveys ##

survey.rename(columns={'dbn': 'DBN'}, inplace=True)

# Filter out columns

columns_to_keep = ["DBN", "rr_s", "rr_t", "rr_p", "N_s", "N_t", 
                   "N_p", "saf_p_11", "com_p_11", "eng_p_11", 
                   "aca_p_11", "saf_t_11", "com_t_11", "eng_t_11", 
                   "aca_t_11", "saf_s_11", "com_s_11", "eng_s_11", 
                   "aca_s_11", "saf_tot_11", "com_tot_11", 
                   "eng_tot_11", "aca_tot_11"]

survey = survey[columns_to_keep]
data['survey'] = survey

## 11. Inserting DBN Fields ##

def pad_if_single_dig(digit):
    """Returns a single digit number padded with 0 on the left. 
    Converts unchanged number to string if more than one digit."""
    
    if len(str(digit)) == 1:
        return str(digit).zfill(2)
    else:
        return str(digit)

# Rename 'dbn' column in hs_directory to 'DBN'
data['hs_directory'].rename(columns={'dbn': 'DBN'}, inplace=True)

# Create DBN column in class_size
data['class_size']['DBN'] = data['class_size']['CSD'].apply(pad_if_single_dig) + data['class_size']['SCHOOL CODE']

data['class_size'].head(3)

## 12. Combining the SAT Scores ##

cols = ['SAT Math Avg. Score', 'SAT Critical Reading Avg. Score', 'SAT Writing Avg. Score']

s1 = pd.to_numeric(data['sat_results'][cols[0]], errors='coerce')
s2 = pd.to_numeric(data['sat_results'][cols[1]], errors='coerce')
s3 = pd.to_numeric(data['sat_results'][cols[2]], errors='coerce')

data['sat_results']['sat_score'] = s1 + s2 + s3

data['sat_results'].head(3)

## 13. Parsing Geographic Coordinates for Schools ##

import re

def extract_lat(string):
    """Extracts lat, long coordinates of the form (x, y) from a longer string."""
    str_coords = re.findall("\(.+\)", string)[0].split(',')
    lat, lon = float(str_coords[0].replace('(', '')), float(str_coords[1].replace(')', ''))
    return lat

data['hs_directory']['lat'] = data['hs_directory']['Location 1'].apply(extract_lat)


print(data['hs_directory'].head(3))

## 14. Extracting the Longitude ##

import re

def extract_lon(string):
    """Extracts lat, long coordinates of the form (x, y) from a longer string."""
    str_coords = re.findall("\(.+\)", string)[0].split(',')
    lat, lon = float(str_coords[0].replace('(', '')), float(str_coords[1].replace(')', ''))
    return lon

data["hs_directory"]["lon"] = data["hs_directory"]["Location 1"].apply(find_lon)

data["hs_directory"]["lat"] = pd.to_numeric(data["hs_directory"]["lat"], errors="coerce")
data["hs_directory"]["lon"] = pd.to_numeric(data["hs_directory"]["lon"], errors="coerce")

print(data["hs_directory"].head(3))
