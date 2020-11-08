# --------------------------------------------------- 
# Joining Data with pandas - Merging Tables with Different Join Types 
# 07 nov 2020 
# VNTBJR 
# --------------------------------------------------- 
# 

######################################################################
# Left Join  -------------------------------------------
######################################################################
# A left join returns all rows of data from the left table and only those rows from 
# the right table where key columns match.
# Counting missing rows with left join
# Load module
import pandas as pd

# Load data
movies = pd.read_pickle('Datasets/movies.p')
financials = pd.read_pickle('Datasets/financials.p')

# Get data info
movies.info()
financials.info()

# What column is likely the best column to merge the two tables on?
# id column

# Merge movies and financials with a left join
movies_financials = movies.merge(right = financials, on = 'id', how = 'left')

# Count the number of rows in the budget column that are missing
number_of_missing_fin = movies_financials['budget'].isna().sum()

# Print the number of movies missing financials
print(number_of_missing_fin)

# Enriching a dataset
# Load data
toy_story = movies[movies['id'].isin(['10193', '863', '862'])]
taglines = pd.read_pickle('Datasets/taglines.p')

# Get data info 
taglines.info()

# Merge the toy_story and taglines tables with a left join
toystory_tag = toy_story.merge(right = taglines, on = 'id', how = 'left')

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)

# Merge the toy_story and taglines tables with a inner join
toystory_tag = toy_story.merge(right = taglines, on = 'id')

# Print the rows and shape of toystory_tag
print(toystory_tag)
print(toystory_tag.shape)

# If your goal is to enhance or enrich a dataset, then you do not want to any of 
# original data. A left join will do what that by returning all of the rows of your 
# left table, while using an inner join may result in lost data if it does not exist 
# in both talbles

######################################################################
# Other joins  -------------------------------------------
###################################################################### 
# A right join is the mirror opposite of a left join. It will return all of the rows 
# from the right table and include only those rows from the left table that have
# matching values.
# An outer join will return all of the rows from both tables regardless of there is 
# a match between the tables.
# Right join to find unique movies
# Load data
genres = pd.read_pickle('Datasets/movie_to_genres.p')
movie_to_genres = movies.merge(right = genres, left_on = 'id', right_on = 'movie_id')
scifi_movies = movie_to_genres.loc[movie_to_genres['genre'] == 'Science Fiction', ['movie_id', 'genre']]
action_movies = movie_to_genres.loc[movie_to_genres['genre'] == 'Action', ['movie_id', 'genre']]

# Get data info
movies.info()
movie_to_genres.info()
scifi_movies.info()
action_movies.info()

# Merge action_movies to scifi_movies with right join
action_scifi = action_movies.merge(right = scifi_movies, on = 'movie_id', how = 'right')

# Merge action_movies to scifi_movies with right join
action_scifi = action_movies.merge(scifi_movies, on = 'movie_id', how = 'right', suffixes = ('_act', '_sci'))

# Print the first few rows of action_scifi to see the structure
print(action_scifi.head())

# From action_scifi, select only the rows where the genre_act column is null
scifi_only = action_scifi[action_scifi['genre_act'].isna()]

# Merge the movies and scifi_only tables with an inner join
movies_and_scifi_only = movies.merge(right = scifi_only, left_on = 'id', right_on = 'movie_id')

# Print the first few rows and shape of movies_and_scifi_only
print(movies_and_scifi_only.head())
print(movies_and_scifi_only.shape)

movies.info()

# Popular genres with right join
# Load modules
import matplotlib.pyplot as plt

# Load data
pop_movies = movies.sort_values('popularity', ascending = False).iloc[:10]
movie_to_genres = movie_to_genres.iloc[:, 4:6]
# Use right join to merge the movie_to_genres and pop_movies tables
genres_movies = movie_to_genres.merge(right = pop_movies, how = 'right', 
                                      left_on = 'movie_id', 
                                      right_on = 'id')

# Count the number of genres
genre_count = genres_movies.groupby('genre').agg({'id':'count'})

# Plot a bar chart of the genre_count
genre_count.plot(kind = 'bar')
plt.show()
plt.clf()

# Using outer join to select actors
# Load data
casts = pd.read_pickle('Datasets/casts.p')
movies.head()
movies_casts = movies.merge(right = casts, left_on = 'id', right_on = 'movie_id', how = 'right', suffixes = ('_movies', ''))
iron_1_actors = movies_casts.loc[movies_casts['title'].isin(['Iron Man']), ['character', 'id', 'name']]
iron_2_actors = movies_casts.loc[movies_casts['title'].isin(['Iron Man 2']), ['character', 'id', 'name']]
movies_casts.loc[movies_casts['title'].isin(['Iron Man']), ['character', 'id', 'name']]
movies_casts.loc[movies_casts['title'].isin(['Iron Man'])].head()
# Get data info
iron_1_actors.head()
iron_2_actors.head()

# Merge iron_1_actors to iron_2_actors on id with outer join using suffixes
iron_1_and_2 = iron_1_actors.merge(right = iron_2_actors,
                                     on = 'id',
                                     how = 'outer',
                                     suffixes = ('_1', '_2'))

# Create an index that returns true if name_1 or name_2 are null
m = ((iron_1_and_2['name_1'].isnull()) | 
     (iron_1_and_2['name_2'].isnull()))

# Print the first few rows of iron_1_and_2
print(iron_1_and_2[m].head())

######################################################################
# Merging a table to itself  -------------------------------------------
######################################################################
# You might need to merge a table to itself when working with tables that have a 
# hierachical relationship, like employee and manager. You might use this on 
# sequential relationships such as logistic movements. Graph data, such as networks
# of friends, might also require this technique.
# Self join
# Load data
crews = pd.read_pickle('Datasets/crews.p')

# Get data info
crews.info()

# Merge the crews table to itself
crews_self_merged = crews.merge(right = crews, on = 'id', suffixes = ('_dir', '_crew'))

# Create a Boolean index to select the appropriate
boolean_filter = ((crews_self_merged['job_dir'] == 'Director') & 
     (crews_self_merged['job_crew'] != 'Director'))
direct_crews = crews_self_merged[boolean_filter]

# Print the first few rows of direct_crews
print(direct_crews.head())

######################################################################
# Merging on indexes  -------------------------------------------
######################################################################
# Index merge for movie ratings
# Load data
ratings = pd.read_pickle('Datasets/ratings.p', )
ratings = ratings.set_index('id')
movies = movies.set_index('id')

# Merge to the movies table the ratings table on the index
movies_ratings = movies.merge(right = ratings, on = 'id', how = 'left')

# Print the first few rows of movies_ratings
print(movies_ratings.head())

# Do sequels earn more?
#Load data
sequels = pd.read_pickle('Datasets/sequels.p')
sequels = sequels.set_index('id')
financials = financials.set_index('id')

# Merge sequels and financials on index id
sequels_fin = sequels.merge(right = financials, on = 'id', how = 'left')

# Self merge with suffixes as inner join with left on sequel and right on id
orig_seq = sequels_fin.merge(sequels_fin, how = 'inner', left_on = 'sequel', 
                             right_on = 'id', right_index = True,
                             suffixes = ('_org', '_seq'))

# Add calculation to subtract revenue_org from revenue_seq 
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']

# Select the title_org, title_seq, and diff 
titles_diff = orig_seq[['title_org', 'title_seq', 'diff']]

# Print the first rows of the sorted titles_diff
print(titles_diff.sort_values('diff', ascending = False).head())
