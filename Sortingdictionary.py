markdict = {"Tom":67, "Tina": 54, "Akbar": 87, "Kane": 43, "Divya":73}
marklist = sorted(markdict.items(), key=lambda x:x[0])
sortdict = dict(marklist)
print(sortdict)