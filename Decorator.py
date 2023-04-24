def chec(func):
    def inner(a,b):
        if b==0:
            print("zero diviosn")
            return
        return func(a,b)
    return inner
@chec
def div(a,b):
    f=a/b
    print(f)
div(6,0)