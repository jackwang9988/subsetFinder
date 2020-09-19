# recursive sum function


def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //=10
    return s


def findSums2(original, start, end):
    for i in range(start, end, -1):
        if i % 2000 == 1:
            print(i)
        solutions[i] = []
        findSubset(original, i)
        if len(solutions[i]) < 2:
            del solutions[i]


def findSubset(nums, target, partial=[]):
    s = sum(partial)
    # check if the partial sum is equals to target
    if s == target:
        if partial not in solutions[s]:
            solutions[s].append(partial)
    if s >= target:
        return  # no point in adding more numbers after sum is greater than target or is target

    for i in range(len(nums)):
        n = nums[i]
        remaining = nums[i + 1:]
        findSubset(remaining, target, partial + [n])


# main
if __name__ == '__main__':
    infile = open('Numbers.txt', 'r')  # full list of numbers
    # infile = open('short.txt', 'r')  # short list of numbers to test with
    lines = infile.readlines()
    infile.close()

    # creating list of numbers
    numbers = []
    index = 0
    sums = []  # list of number sums
    s138 = []

    for line in lines:
        line = line.strip()
        numbers.append(int(line))

    print("List of Numbers and their digit sums:\n")
    for number in numbers:
        tmp = sum_digits(number)
        sums.append(tmp)
        if tmp == 138:
            s138.append(number)
        print("Number: {} | Sum: {}".format(number, tmp))
    sums.sort()
    print(sums)
    print(s138)

    numbers.sort()
    smallest = min(numbers)
    total = 0
    index = 0

    print("\nList of Numbers:\n")
    for number in numbers:
        total += number
        print("Index {}: {}".format(index, number))
        index += 1
    print("Total: " + str(total))

    iterations = 0
    solutions = {}
    # findSums(numbers, numbers)
    # findSums2(numbers, total, smallest)

    # prints the solutions
    sol = 0
    for key in solutions:
        if len(solutions[key]) > 1:
            print("Solutions for sum: " + str(key))
            print(solutions[key])
            sol += 1

    if sol == 0:
        print("No Solutions")
