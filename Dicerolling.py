import Sortingdictionary
minv=1
maxv=6
choice=input("rollagain")
while choice=="yes" or choice=="y":
    print("rolling the dice")
    print("the score on first dice is",random.randint(minv,maxv))
    print("the score on first dice is", random.randint(minv, maxv))
    choice = input("rollagain")

