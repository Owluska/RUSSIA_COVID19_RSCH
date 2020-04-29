Load data 'covid19-russia-regions-cases\covid19-russia-cases.csv', shape: (1661, 10) 
Columns list: ['Date', 'Region/City', 'Region/City-Eng', 'Region_ID', 'Day-Confirmed', 'Day-Deaths', 'Day-Recovered', 'Confirmed', 'Deaths', 'Recovered']

Load data 'covid19-russia-regions-cases\covid19-tests-and-other.csv', shape: (85, 10) 
Columns list: ['Date', 'Tests', 'Control', 'Control_active', 'Isolated', 'Imported_SARS', 'Recovered', 'Isolators', 'Isolators_active', 'Mos_self_isolat_idx']

Load data 'covid19-russia-regions-cases\moscow_addresses.csv', shape: (697, 3) 
Columns list: ['Address', 'Latitude', 'Longitude']

Load data 'covid19-russia-regions-cases\regions-info.csv', shape: (86, 14) 
Columns list: ['Region_ID', 'Region', 'Region_eng', 'Population', 'Rus_perc', 'Urban_pop', 'Urban_pop_perc', 'Rural_pop', 'Rural_pop_perc', 'Area', 'Density_pop_sqkm', 'Federal_district', 'Latitude', 'Longitude']

Load data 'covid19-russia-regions-cases\regions-ventilators.csv', shape: (66, 7) 
Columns list: ['Region', 'Region_eng', 'Vent_idx', 'Vent_num', 'ECMO_idx', 'ECMO_num', 'Region_ID']

Data after concat, shape: (2595, 36) 
Columns list: ['Date', 'Region/City', 'Region/City-Eng', 'Region_ID', 'Day-Confirmed', 'Day-Deaths', 'Day-Recovered', 'Confirmed', 'Deaths', 'Recovered', 'Tests', 'Control', 'Control_active', 'Isolated', 'Imported_SARS', 'Isolators', 'Isolators_active', 'Mos_self_isolat_idx', 'Address', 'Latitude', 'Longitude', 'Region', 'Region_eng', 'Population', 'Rus_perc', 'Urban_pop', 'Urban_pop_perc', 'Rural_pop', 'Rural_pop_perc', 'Area', 'Density_pop_sqkm', 'Federal_district', 'Vent_idx', 'Vent_num', 'ECMO_idx', 'ECMO_num']

         Region_ID  Day-Confirmed  ...   ECMO_idx    ECMO_num
count  1807.000000    1661.000000  ...  41.000000   41.000000
mean     44.913116      34.926550  ...   0.115854    6.048780
std      24.489645     193.702674  ...   0.100498   19.806503
min       0.000000       0.000000  ...   0.000000    0.000000
25%      25.000000       1.000000  ...   0.050000    1.000000
50%      46.000000       5.000000  ...   0.080000    1.000000
75%      65.000000      18.000000  ...   0.160000    2.000000
max      95.000000    3570.000000  ...   0.460000  124.000000

[8 rows x 25 columns]