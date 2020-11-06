# --------------------------------------------------- 
# Joining Data with Pandas - Data Merging Basics 
# 06 nov 2020 
# VNTBJR 
# --------------------------------------------------- 
#

######################################################################
# Inner join  -------------------------------------------
######################################################################
# The pandas pckage has an method to for performing merge called merge. The merge 
# method takes the first DataFrame, and merges it with the secind DataFrame, and uses 
# the "on" argument totell the method that we want to merge the two DataFrames on the
# column we specify. A inner join will only return rows that have matching values in 
# both tables.
# To avoid multiple columns with the same name, are automatically, or manually, given 
# a suffix by the merge method. To provide suffix manually, we provide a tuple where 
# all of the overlapping columns in the left table are given one suffix, and those of 
# the rigth table will be given another suffix.
# 
# Your first inner join
# load data
import pandas as pd
taxi_owners = pd.read_pickle('Datasets/taxi_owners.p')
taxi_veh = pd.read_pickle('Datasets/taxi_vehicles.p')

# Get data info
taxi_owners.info()
taxi_veh.info()

# Merge the taxi_owners and taxi_veh tables
taxi_own_veh = taxi_owners.merge(right = taxi_veh, on = 'vid')

# Print the column names of the taxi_own_veh
print(taxi_own_veh.columns)

# Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(taxi_veh, on = 'vid', suffixes = ('_own', '_veh'))

# Print the column names of taxi_own_veh
print(taxi_own_veh.columns)

# Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(taxi_veh, on = 'vid', suffixes = ('_own', '_veh'))

# Print the value_counts to find the most popular fuel_type
print(taxi_own_veh['fuel_type'].value_counts())

# Inner joins and number of rows returned
# load data
wards = pd.read_pickle('Datasets/ward.p')
census = pd.read_pickle('Datasets/census.p')

# Get data info
wards.info()
census.info()

# Merge the wards and census tables on the ward column
wards_census = wards.merge(right = census, on = 'ward')

# Print the shape of wards_census
print(wards_census.shape)

# In the ward column change '1' to '61'
wards.loc[wards['ward'] == '1', 'ward'] = '61'

# Merge the wards and census tables on the ward column
wards_census = wards.merge(census, on = 'ward')

# Print the shape of wards_census
print(wards_census.shape)

# Change '1' to None in `ward` col
census.loc[census['ward'] == '1', 'ward'] = None

# Merge the wards and census tables on the ward column
wards_census = wards.merge(census, on = 'ward')

# Print the shape of wards_census
print(wards_census.shape)

######################################################################
# One to many relationships  -------------------------------------------
######################################################################
# In one-to-one relationship, every row in the left table is related to one and 
# only one row in the right table.
# In a one-to-many relationship, every row in the left table is related to one or
# more rows in the table.
# 
# One-to-many merge
# load data
biz_owners = pd.read_pickle('Datasets/business_owners.p')
licenses = pd.read_pickle('Datasets/licenses.p')

# Get data info
biz_owners.info()
licenses.info()

# Merge the licenses and biz_owners table on account
licenses_owners = licenses.merge(right = biz_owners, on = 'account')

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby('title').agg({'account':'count'})

# Sort the counted_df in desending order
sorted_df = counted_df.sort_values('account', ascending = False)

# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head())

######################################################################
# Merging multiple DataFrames  -------------------------------------------
######################################################################
# Total riders in a month
# Load data
cal = pd.read_pickle('Datasets/cta_calendar.p')
ridership = pd.read_pickle('Datasets/cta_ridership.p')
stations = pd.read_pickle('Datasets/stations.p')

# Get data info
cal.info()
ridership.info()
stations.info()

# Merge the ridership and cal tables
ridership_cal = ridership.merge(right = cal, on = ['year', 'month', 'day'])

# Merge the ridership, cal, and stations tables
ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \
            				.merge(right = stations, on = 'station_id')
            				
# Create a filter to filter ridership_cal_stations
filter_criteria = ((ridership_cal_stations['month'] == 7) 
                   & (ridership_cal_stations['day_type'] == 'Weekday') 
                   & (ridership_cal_stations['station_name'] == 'Wilson'))

# Use .loc and the filter to select for rides
print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())

# Three table merge
# Load data
zip_demo = pd.read_pickle('Datasets/zip_demo.p')

# Get data info
zip_demo.info()

# Merge licenses and zip_demo, on zip; and merge the wards on ward
licenses_zip_ward = licenses.merge(right = zip_demo, on = 'zip') \
            			.merge(right = wards, on = 'ward')

# Print the results by alderman and show median income
print(licenses_zip_ward.groupby('alderman').agg({'income':'median'}))

# One-to-many merge with multiple tables
# Load data
land_use = pd.read_pickle('Datasets/land_use.p')

# Get data info
land_use.info()

# Merge land_use and census and merge result with licenses including suffixes
land_cen_lic = land_use.merge(right = census, on = 'ward') \ 
                       .merge(right = licenses, on = 'ward', suffixes = ('_cen', '_lic'))

# Group by ward, pop_2010, and vacant, then count the # of accounts
pop_vac_lic = land_cen_lic.groupby(['ward', 'pop_2010', 'vacant'], 
                                   as_index=False).agg({'account':'count'})
                                   
# Sort pop_vac_lic and print the results
sorted_pop_vac_lic = pop_vac_lic.sort_values(['vacant', 'account', 'pop_2010'], 
                                             ascending = [False, True, True])

# Print the top few rows of sorted_pop_vac_lic
print(sorted_pop_vac_lic.head())
