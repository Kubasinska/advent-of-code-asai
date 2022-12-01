import time
tic = time.time()

with open("input.txt") as file:
    data = file.readlines()

this_elve = list()
max_calories = 0
for element in data:
    if element[:-1].isdecimal():
        this_elve.append(int(element))
    else:
        this_elve_sum = sum(this_elve)
        if this_elve_sum >= max_calories:
            max_calories = this_elve_sum

        this_elve = list()

print(max_calories)

print(time.time() - tic)
