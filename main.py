import time
tic = time.time()

with open("input.txt") as file:
    data = file.readlines()

all_elves = list()
this_elve = list()
max_calories = 0
for element in data:
    if element[:-1].isdecimal():
        this_elve.append(int(element))
    else:
        this_elve_sum = sum(this_elve)
        if this_elve_sum >= max_calories:
            max_calories = this_elve_sum
        all_elves.append(this_elve_sum)
        this_elve = list()


top_three_sum = sum(sorted(all_elves, reverse=True)[:2])
print(f"Solution 1:{max_calories}")
print(f"Solution 2:{top_three_sum}")
print(time.time() - tic)
