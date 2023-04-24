def doublenbr(a):
    return a+a
l=(1,2,3,4,5)
l1=map(doublenbr,l)
print(list(l1))
#the following shows to use lambda expression with map function
l2=map(lambda a:a+a,l)
print(list(l2))
#add two lists using map and lambda
list1=[1,2,3,4,5]
list2=[1,2,3,4,5]
ad=map(lambda a,b:a+b, list1,list2)
print(list(ad))
# List of strings
l = ['sat', 'bat', 'cat', 'mat']
# map() can listify the list of strings individually
test = list(map(list, l))
print(test)
#Define a function that doubles even numbers and leaves odd numbers as is
# Define a function that doubles even numbers and leaves odd numbers as is
def double_even(num):
	if num % 2 == 0:
		return num * 2
	else:
		return num

# Create a list of numbers to apply the function to
numbers = [1, 2, 3, 4, 5]

# Use map to apply the function to each element in the list
result = list(map(double_even, numbers))

# Print the result
print(result) # [1, 4, 3, 8, 5]

def myfunc(n):
  return len(n)
hj=('apple', 'banana', 'cherry')
x = map(myfunc, hj)
print(list(x))

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(lambda s: s[0] == "A", fruit)

print(list(map_object))