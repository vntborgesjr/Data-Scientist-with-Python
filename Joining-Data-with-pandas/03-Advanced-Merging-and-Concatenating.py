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
