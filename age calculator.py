def ageCalculator(y, m, d):
    import datetime
    today = datetime.datetime.now().date()
    today1 = datetime.datetime.now()
    print(today)
    print(today1)
    dob = datetime.date(y, m, d)
    age = int((today-dob).days / 365.25)
    print(age)
ageCalculator(1990, 9, 7)