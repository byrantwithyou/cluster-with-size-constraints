import random
random.seed()
file = open("data.txt", "w")
for i in range(100):
  print(random.uniform(0, 100), random.uniform(0, 100), sep=",", file=file)
