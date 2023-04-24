#Dictionary Comprehension
sdict=dict()
for i in range(10):
    sdict[i]=i*i
print(sdict)
#dictionary comprehension example
sdict1={i:i*i for i in range(11)}
print(sdict1)
#multipy values by a number
#item price in dollars
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
new_price={item:value*10 for (item,value) in old_price.items()}
print(new_price)
#If Conditional Dictionary Comprehension
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
c_dict={j:k for (j,k) in original_dict.items() if k%2==0}
print(c_dict)
#Multiple if Conditional Dictionary Comprehension
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
new_dict = {k: v for (k, v) in original_dict.items() if v % 2 != 0 if v < 40}
print(new_dict)
#if-else Conditional Dictionary Comprehension
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
c_d={k:("old" if v > 40 else "young") for (k,v) in original_dict.items()}
print(c_d)
#Nested Dictionary with Two Dictionary Comprehensions
dictionary = {
    k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2, 5)
}
print(dictionary)




