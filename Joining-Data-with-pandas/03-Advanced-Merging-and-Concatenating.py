# --------------------------------------------------- 
# Joining Data with pandas - Advanced Merging and Concatenating 
# 07 nov 2020 
# VNTBJR 
# --------------------------------------------------- 
#

######################################################################
# Filtering joins  -------------------------------------------
######################################################################
# So far, we have only worked with mutating joins, which combines data from two 
# tables on matching observatinos in both tables.
# Filtering joins filter observations from one table based on whether or not they 
# match an observation in another table.
# A SEMI-JOIN fliters the left table down to those observations that have a match in
# the right table. It is simmilar to an inner join where only the intersction
# between the tables is returned, but unlike an inner join, only the columns from the 
# left table are shown. No duplicate rows from the left table are returned, even if 
# there is a one-to-one relationship.
# Steps of a SEMI-JOIN:
# 1 - Merge the leeft and right tables on key column using an inner-join;
# 2- Search if the key column in the left table is in the merged tables using the
# .isin() mthod creating a Boolean Series;
# 3 - Subset the rows of the left table.
# An ANTI-JOIN returns the observations in the left table that do not have a matching 
# observation in the right table. It only returns the columns from the left table.
# Performing an anti-join
# No data available for this practice...
# Merge employees and top_cust
empl_cust = employees.merge(right = top_cust, on = 'srid', 
                            how = 'left', indicator = True)

# Select the srid column where _merge is left_only
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']

# Get employees not working with top customers
print(employees[employees['srid'].isin(srid_list)])

# Performing a semi-join
# No data available for this practice...
# Merge the non_mus_tck and top_invoices tables on tid
tracks_invoices = non_mus_tcks.merge(right = top_invoices, on = 'tid')

# Use .isin() to subset non_mus_tcks to rows with tid in tracks_invoices
top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]

# Group the top_tracks by gid and count the tid rows
cnt_by_gid = top_tracks.groupby(['gid'], as_index = False).agg({'tid': 'count'})

# Merge the genres table to cnt_by_gid on gid and print
print(cnt_by_gid.merge(right = genres, on = 'gid'))

######################################################################
# Concatenate DataFrames together vertically  -------------------------------------------
######################################################################
# Concatenation basics
# No data available for this practice...
# Concatenate the tracks
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               sort = True)
print(tracks_from_albums)

# Concatenate the tracks so the index goes from 0 to n-1
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               ignore_index = True,
                               sort = True)
print(tracks_from_albums)

# Concatenate the tracks, show only columns names that are in all tables
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               join = 'inner',
                               sort = True)
print(tracks_from_albums)

# Concatenating with keys
# No data available for this practice...
# Concatenate the tables and add keys
inv_jul_thr_sep = pd.concat([inv_jul, inv_aug, inv_sep], 
                            keys = ['7Jul', '8Aug', '9Sep'])

# Group the invoices by the index keys and find avg of the total column
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total': 'mean'})

# Bar plot of avg_inv_by_month
avg_inv_by_month.plot(kind = 'bar')
plt.show()
plt.clf()

# Using the append method
# No data available for this practice...
# Use the .append() method to combine the tracks tables
metallica_tracks = tracks_ride.append([tracks_master, tracks_st], sort = False)

# Merge metallica_tracks and invoice_items
tracks_invoices = metallica_tracks.merge(right = invoice_items, on = 'tid')

# For each tid and name sum the quantity sold
tracks_sold = tracks_invoices.groupby(['tid','name']).agg({'quantity': 'sum'})

# Sort in decending order by quantity and print the results
print(tracks_sold.sort_values('quantity', ascending = False))

######################################################################
# Verifying integrity  -------------------------------------------
######################################################################
# Concatenate and merge to find common songs
# Concatenate the classic tables vertically
classic_18_19 = pd.concat([classic_18, classic_19], ignore_index = True)

# Concatenate the pop tables vertically
pop_18_19 = pd.concat([pop_18, pop_19], ignore_index = True)

# Merge classic_18_19 with pop_18_19
classic_pop = classic_18_19.merge(right = pop_18_19, on = 'tid')

# Using .isin(), filter classic_18_19 rows where tid is in classic_pop
popular_classic = classic_18_19[classic_18_19['tid'].isin(classic_pop['tid'])]

# Print popular chart
print(popular_classic)
