#create nested dictionary
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people)
#Access the elements using the [] syntax
print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])
print(people[2]['name'])
print(people[2]['age'])
print(people[2]['sex'])
#How to change or add elements in a nested dictionary?
people[3]={}
people[3]['name']='durga'
people[3]['age']=30
people[3]['sex']='male'
people[3]['married'] = 'No'
print(people[3])
print(people)
#How to delete elements from a nested dictionary
del people[3]['married']
print(people[3])
#How to delete dictionary from a nested dictionary
del people[3]
print(people)
#How to iterate through a Nested dictionary
people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}

for p_id, p_info in people.items():
    print("\nPerson ID:", p_id)

    for key in p_info:
        print(key + ':', p_info[key])
"""
Key Points to Remember:
Nested dictionary is an unordered collection of dictionary
Slicing Nested Dictionary is not possible.
We can shrink or grow nested dictionary as need.
Like Dictionary, it also has key and value.
Dictionary are accessed using key.
"""
#multiple inputs at sametime
j=[x for x in input("eneter values").split(",")]
print(j)