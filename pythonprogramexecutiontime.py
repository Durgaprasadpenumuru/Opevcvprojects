from time import time
start = time()

# Python program to create acronyms
word = "Artificial Intelligence"
text = word.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)
print(type(start))

end = time()
print(end)
execution_time = end - start
print("Execution Time : ", execution_time)