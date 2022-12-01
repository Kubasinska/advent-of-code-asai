import time
tic = time.time()

def max_calories(path):
    input_list = open(path).read()
    elves = [sum([int(cal) for cal in calories.split('\n')]) for calories in input_list.split('\n\n')]
    return max(elves)

print(time.time() - tic)
print(max_calories('input.txt'))
