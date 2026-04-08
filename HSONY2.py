import itertools

data = ["Ali", "BMW2000", "Ahmed", "1980", "Alaa","aaa" , "CR7", "Managemet"]

for i in [1,2, 3]:
    for j in itertools.permutations(data, i):
        print ("".join(j))
