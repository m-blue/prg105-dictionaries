# Create a dictionary named holidays that pairs the name of
# the holiday with the date it will occur this year, include at least four
# key-value pairs
# example: holiday = {'Independence Day':  'July 4'}
holidays = dict()
holidays = {'Halloween': 'October 31', 'Thanksgiving' : 'November 25', 'Christmas' : 'December 25', 'New Years Day': 'January 1'}


# print holiday -  does the order match what you put it in?
# Answer: No
print holidays

# run the len function on holiday - how does it calculate the results? ** print(len(holiday))
# Answer: By the amount of key values
print (len(holidays))


# Write the code to use the "in" function to find one of the keys in your dictionary. Make sure to surround the
# code with a print statement so that the result prints on screen
print ('Halloween' in holidays)


# now write the code to look for a key that is not in the dictionary. Make sure to surround the code
# with a print statement so the result prints on screen
print ('Arbor Day' in holidays)



# now write the code to find a value in your dictionary, use the print statement to show the results
vals = holidays.values()
print ('December 25' in vals)

# print all of the values in the dictionary
print vals


# 11.2 Looping and Dictionaries
# Write the histogram code and test it by passing in a word that has at least two of one letter
# Print the result of running the histogram code

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

print (histogram('kitty'))

# Exercise 11.2 Rewrite the histogram code using the get method, test with the same word, name the function histogram2
# hint assign the result of d.get(c,0) to a value then add one to the value of d[c]

def histogram2(s):
    d = dict()
    for c in s:
        if d.get(c,0):
            d[c] = 1
        else:
            d[c] += 1
    return d

print (histogram('kitty'))


# Looping and Dictionaries
# use a for statement to print your holiday dictionary
# What prints? The keys or the values? Answer: Value
for f in holidays:
    print holidays[f]



print ("\n\n\n")  # leave this code so that there are blank lines before the next exercise
# now write code that prints all of the keys and all of their values in the holiday dictionary
# if you use the print statement then values separated by commas they appear on the same line

print holidays


print ("\n\n\n")  # leave this code so that there are blank lines before the next exercise
# Reverse Lookup
# Type the code for the Reverse Lookup from 11.3 below
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError

# Test the code by calling it with the holiday dictionary and one of your values (print the result)
print (reverse_lookup(holidays,'December 25'))

# Call the code a second time with a value that doesn't exist, run the program

#print (reverse_lookup(holidays,'October 10'))

# Copy and paste the error code here, add # as needed to make the error a comment

#Traceback (most recent call last):
 # File "C:/Users/Mark.Mark-PC/Documents/PRG 105/dictionaries-1.py", line 94, in <module>
  #  print (reverse_lookup(holidays,'October 10'))
  #File "C:/Users/Mark.Mark-PC/Documents/PRG 105/dictionaries-1.py", line 88, in reverse_lookup
   # raise ValueError
#ValueError

# leave the line of code that caused the error, but put a # in front of it to make it a comment


# 11.4 Dictionaries and lists
# Type in the code to invert a dictionary
# Call the invert_dict function with the holiday dictionary
# print the results
print ("\n\n")

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

print (invert_dict(holidays))

print ("\n\n")
# Exercise 11.5 Exercise 11.5. Read the documentation of the dictionary method setdefault and use it to write a
# more concise version of invert_dict. Solution: http://thinkpython.com/code/invert_dict. py .

def invert_dict2(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, key)
    return inverse

print (invert_dict2(holidays))
