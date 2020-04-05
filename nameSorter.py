with open("Sort Me.txt") as file:
    names = [line.strip() for line in file]
names.sort()
names.sort(key=len)
for name in names:
    print(name)
