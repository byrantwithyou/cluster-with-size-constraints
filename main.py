data = []
with open("data.txt", "r") as file:
    data = [(float(line[:line.find(",")]), float(line[line.find(",") + 1: -1])) for line in file]
