####################################################
# Python Data Science Toolbox (Part 1) - Default arguments, variable-length arguments and scope
# 29 Out 2020
# VNTBJR
####################################################
#
# Load packages
library(reticulate)

####################################################
# Scope and user-defined functions ------------------------------
####################################################
#
# Scope - part of the program where an object or name may be accessible
# There area three types of scope:
# Golbal scope defined in the main body os a script
# Local scope - defined inside da function (once the exectution of a function is
# done, any name inside the local scope ceades to exist)
# Built-in scope - names in the pre-defined built-ins modules

# Pop quiz on understanding scope
num = 5
def func1():
  num = 3
  print(num)
quit()

def func2():
  global num
  double_num = num * 2
  num = 6
  print(double_num)
quit()
func1()
func2()
num

# The keyword golbal
# Create a string: team
team = "teen titans"

# Define change_team()
def change_team():
    """Change the value of the global variable team."""
    # Use team in global scope
    global team
    # Change the value of team in global: team
    team = 'justice league'
# Print team
print(team)
quit()
# Call change_team()
change_team()

# Print team
print(team)

# Python built-in scope
import builtins
dir(builtins)

####################################################
# Nested functions ------------------------------
####################################################
#
# Nested functions I
# Define three_shouts
def three_shouts(word1, word2, word3):
    """Returns a tuple of strings
    concatenated with '!!!'."""
    # Define inner
    def inner(word):
        """Returns a string concatenated with '!!!'."""
        return word + '!!!'
    # Return a tuple of strings
    return (inner(word1), inner(word2), inner(word3))
quit()
# Call three_shouts() and print
print(three_shouts('a', 'b', 'c'))

# Nested functions II
# Define echo
def echo(n):
    """Return the inner_echo function."""
    # Define inner_echo
    def inner_echo(word1):
        """Concatenate n copies of word1."""
        echo_word = word1 * n
        return echo_word
    # Return inner_echo
    return (inner_echo)
quit()
# Call echo: twice
twice = echo(2)

# Call echo: thrice
thrice = echo(3)

# Call twice() and thrice() then print
print(twice('hello'), thrice('hello'))

# The keyword nonlocal and nested functions
# Define echo_shout()
def echo_shout(word):
    """Change the value of a nonlocal variable"""
    # Concatenate word with itself: echo_word
    echo_word = word + word
    # Print echo_word
    print(echo_word)
    # Define inner function shout()
    def shout():
        """Alter a variable in the enclosing scope"""    
        # Use echo_word in nonlocal scope
        nonlocal echo_word
        # Change echo_word to echo_word concatenated with '!!!'
        echo_word = echo_word + '!!!'
    # Call function shout()
    shout()
    # Print echo_word
    print(echo_word)
quit()
# Call function echo_shout() with argument 'hello'
echo_shout('hello')

####################################################
# Default and flexible arguments ------------------------------
####################################################
#
# Functions with one default argument
# Define shout_echo
def shout_echo(word1, echo = 1):
    """Concatenate echo copies of word1 and three
     exclamation marks at the end of the string."""
    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo
    # Concatenate '!!!' to echo_word: shout_word
    shout_word = echo_word + '!!!'
    # Return shout_word
    return shout_word
quit()
# Call shout_echo() with "Hey": no_echo
no_echo = shout_echo('Hey')

# Call shout_echo() with "Hey" and echo=5: with_echo
with_echo = shout_echo('Hey', 5)

# Print no_echo and with_echo
print(no_echo)
print(with_echo)

# Functions with multiple default arguments
# Define shout_echo
def shout_echo(word1, echo = 1, intense = False):
    """Concatenate echo copies of word1 and three
    exclamation marks at the end of the string."""
    # Concatenate echo copies of word1 using *: echo_word
    echo_word = word1 * echo
    # Make echo_word uppercase if intense is True
    if intense is True:
        # Make uppercase and concatenate '!!!': echo_word_new
        echo_word_new = echo_word.upper() + '!!!'
    else:
        # Concatenate '!!!' to echo_word: echo_word_new
        echo_word_new = echo_word + '!!!'
    # Return echo_word_new
    return echo_word_new
quit()
# Call shout_echo() with "Hey", echo=5 and intense=True: with_big_echo
with_big_echo = shout_echo('Hey', 5, True)

# Call shout_echo() with "Hey" and intense=True: big_no_echo
big_no_echo = shout_echo('Hey', intense = True)

# Print values
print(with_big_echo)
print(big_no_echo)

# Functions with variable-length arguments (*args)
# Define gibberish
def gibberish(*args):
    """Concatenate strings in *args together."""
    # Initialize an empty string: hodgepodge
    hodgepodge = str()
    # Concatenate the strings in args
    for word in args:
        hodgepodge += word
    # Return hodgepodge
    return hodgepodge
quit()
# Call gibberish() with one string: one_word
one_word = gibberish('luke')

# Call gibberish() with five strings: many_words
many_words = gibberish("luke", "leia", "han", "obi", "darth")

# Print one_word and many_words
print(one_word)
print(many_words)

# Functions with variable-length keyword arguments (**kwargs)
# Define report_status
def report_status(**kwargs):
    """Print out the status of a movie character."""
    print("\nBEGIN: REPORT\n")
    # Iterate over the key-value pairs of kwargs
    for key, value in kwargs.items():
        # Print out the keys and values, separated by a colon ':'
        print(key + ": " + value)
    print("\nEND REPORT")
quit()
# First call to report_status()
report_status(name = 'luke', affiliation = 'jedi', status = 'missing')

# Second call to report_status()
report_status(name = 'anakin', affiliation = 'sith lord', status = 'deceased')

####################################################
# Bring it all together ------------------------------
####################################################
#
# Define count_entries()
def count_entries(df, col_name = 'lang'):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    # Initialize an empty dictionary: cols_count
    cols_count = {}
    # Extract column from DataFrame: col
    col = df[col_name]
    # Iterate over the column in DataFrame
    for entry in col:
        # If entry is in cols_count, add 1
        if entry in cols_count.keys():
            cols_count[entry] += 1
        # Else add the entry to cols_count, set the value to 1
        else:
            cols_count[entry] = 1
    # Return the cols_count dictionary
    return cols_count
quit()
# Call count_entries(): result1
result1 = count_entries(tweets_df)

# Call count_entries(): result2
result2 = count_entries(tweets_df, 'source')

# Print result1 and result2
print(result1)
print(result2)

# Bringing all together (2)
# Define count_entries()
def count_entries(df, *args):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    #Initialize an empty dictionary: cols_count
    cols_count = {}
    # Iterate over column names in args
    for col_name in args:
        # Extract column from DataFrame: col
        col = df[col_name]
        # Iterate over the column in DataFrame
        for entry in col:
            # If entry is in cols_count, add 1
            if entry in cols_count.keys():
                cols_count[entry] += 1
                # Else add the entry to cols_count, set the value to 1
            else:
                cols_count[entry] = 1
    # Return the cols_count dictionary
    return cols_count
quit()
# Call count_entries(): result1
result1 = count_entries(tweets_df, 'lang')

# Call count_entries(): result2
result2 = count_entries(tweets_df, 'lang', 'source')

# Print result1 and result2
print(result1)
print(result2)
