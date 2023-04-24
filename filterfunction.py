ages = [5, 12, 17, 18, 24, 32]
def ag(f):
    if f>18:
        return True
    else:
        return False
cat=filter(ag,ages)
for g in cat:
    print(g)
# function that filters vowels
def fun(variable):
	letters = ['a', 'e', 'i', 'o', 'u']
	if (variable in letters):
		return True
	else:
		return False


# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(fun, sequence)

print('The filtered letters are:')
for s in filtered:
	print(s)
# a list contains both even and odd numbers.
seq = [0, 1, 2, 3, 5, 8, 13]

# result contains odd numbers of the list
result = filter(lambda x: x % 2 != 0, seq)
print(list(result))

# result contains even numbers of the list
result = filter(lambda x: x % 2 == 0, seq)
print(list(result))

#Define a function to check if a number is a multiple of 3
def is_multiple_of_3(num):
	return num % 3 == 0

# Create a list of numbers to filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter and a lambda function to filter the list of numbers
# and only keep the ones that are multiples of 3
result = list(filter(lambda x: is_multiple_of_3(x), numbers))

# Print the result
print(result) # [3, 6, 9]
#I wrote this to check if a number is positive or not and extract them to a list
kl=[-1,3,-4,-5,6,7]
def is_pos(a):
	if a <0:
		return True
	else:
		return False
fil=filter(is_pos,kl)
print(list(fil))
# Without using lambdas
def starts_with_A(s):
    return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(starts_with_A, fruit)

print(list(filter_object))
fo=filter(lambda x:x[0]=='A',fruit)
print(list(fo))

#Filter Multiple Keys Out of a Python Dictionary
def my_filtering_function(pair):
	wanted_keys = ['John', 'Matt']
	key, value = pair
	if key in wanted_keys:
		return True  # keep pair in the filtered dictionary
	else:
		return False  # filter pair out of the dictionary


grades = {'John': 7.8, 'Mary': 9.0, 'Matt': 8.6, 'Michael': 9.5}

filtered_grades = dict(filter(my_filtering_function, grades.items()))

print(filtered_grades)

#Filter a Python Dictionary by Value
def my_filtering_function(pair):
	key, value = pair
	if value >= 8.5:
		return True  # keep pair in the filtered dictionary
	else:
		return False  # filter pair out of the dictionary


grades = {'John': 7.8, 'Mary': 9.0, 'Matt': 8.6, 'Michael': 9.5}

filtered_grades = dict(filter(my_filtering_function, grades.items()))

print(filtered_grades)

#Filter a Python Dictionary by Multiple Conditions
def my_filtering_function(pair):
	key, value = pair
	if len(key) != 4:  # first condition
		return False
	if key[0] != 'M':
		return False  # second condition
	if value <= 8.9:
		return False  # third condition
	# If nothing was returned until here, it means that
	# the pair passed all conditions. Keep it in the dictionary!
	return True


grades = {'John': 7.8, 'Mary': 9.0, 'Matt': 8.6, 'Michael': 9.5}

filtered_grades = dict(filter(my_filtering_function, grades.items()))

print(filtered_grades)