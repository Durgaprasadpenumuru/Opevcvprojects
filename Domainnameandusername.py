user_input = input("enter email address :")
result = user_input.split('@')
print("username : ",result[0])
print("domain name : ",result[1])